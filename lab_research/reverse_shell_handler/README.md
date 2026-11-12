# Python Reverse Shell – Learning Project

A small Python project I built while learning about socket programming, client-server communication, and remote access concepts in cybersecurity.

This project consists of two scripts, `server.py` and `backdoor.py`, which experiment with establishing a TCP connection between two machines and exchanging data.

I'm still learning how these concepts work, so this project is mainly an experiment to understand the basics of network communication and Python.

## What I Used

- Python 3
- `socket` – For TCP connections and communication.
- `json` – For sending and receiving structured data.
- `os` – For basic operating system and file operations.
- `subprocess` – Explored for process execution in the client-side code.
- `time` – Used for timing and reconnection experiments.

## What I Explored

- Creating TCP sockets and establishing connections.
- Understanding how client-server communication works.
- Sending and receiving data using JSON.
- Basic file handling and binary data transfer.
- Understanding how remote command execution works.
- Learning about connection handling and error management.

## Files

| File | Description |
|---|---|
| `server.py` | Server-side connection handler and communication interface. |
| `backdoor.py` | Client-side communication experiment. |

## Things I Learned

This project helped me get a better understanding of:

- Python socket programming.
- How TCP connections work.
- How two programs communicate over a network.
- JSON serialization.
- Basic file transfer concepts.
- Some security risks associated with remote access tools.

## Current Limitations

There are still plenty of things I need to improve and understand better:

- No encryption in communication.
- No proper authentication.
- Basic error handling.
- Limited connection management.
- File transfers aren't fully reliable.

## Disclaimer

This project was created for learning and experimentation in a controlled lab environment.

It is not intended for unauthorised access to systems or networks.

---

**Author:** Pushkar

*Part of my ongoing journey into Python programming, cybersecurity, and ethical hacking.*
