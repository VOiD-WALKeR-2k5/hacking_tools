# HTTP Directory Discovery Tool

A lightweight Python-based HTTP directory discovery tool that checks for commonly accessible web directories and endpoints using a user-provided wordlist.

## Features

- HTTP endpoint and directory discovery
- Multithreaded requests using ThreadPoolExecutor
- Configurable wordlist
- Identifies HTTP status codes:
  - 200 – OK
  - 301 – Moved Permanently
  - 302 – Found
  - 401 – Unauthorized
  - 403 – Forbidden
- Request timeout handling
- Filters unnecessary output

## Requirements

- Python 3
- Requests library

Install dependencies:

```bash
pip install requests
```

## Usage

Run the script:

```bash
python directory_discovery.py
```

Enter the target URL and the path to your wordlist when prompted.

## How It Works

1. Accepts a target URL.
2. Reads directory names from a user-provided wordlist.
3. Generates HTTP requests for each directory.
4. Uses ThreadPoolExecutor to execute multiple requests concurrently.
5. Filters and displays responses with selected HTTP status codes.

## Limitations

- Results depend on the supplied wordlist.
- HTTP responses do not always indicate whether a resource actually exists.
- Network restrictions and server configurations can affect results.

## Disclaimer

This tool is intended for educational purposes and authorised security testing only. Only test systems for which you have explicit permission.

## Author

Pushkar

Part of the `hacking_tools` collection.
