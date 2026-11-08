# Multithreaded Web Directory Scanner

A lightweight Python security utility designed for rapid web path discovery and HTTP endpoint enumeration.

## Features

- **Concurrent Execution:** Uses `concurrent.futures.ThreadPoolExecutor` to handle up to 10 concurrent connections.
- **Response Filtering:** Excludes non-essential response codes and highlights active endpoints (`200 OK`, `301/302 Redirects`, `401 Unauthorized`, `403 Forbidden`).
- **Controlled Redirects:** Disables automatic redirection (`allow_redirects=False`) to expose hidden login targets and route changes.
- **Fault Tolerance:** Catches socket errors, DNS failures, and connection timeouts cleanly without interrupting active threads.

## Requirements

- Python 3.x
- `requests` library

```bash
pip install requests
