# Login Authentication Tester – Learning Project

A small Python project I built while learning about HTTP requests, web authentication, and basic security testing.

This project experiments with sending HTTP POST requests to a login endpoint using passwords from a text file. It also uses multithreading to understand how multiple requests can be handled concurrently.

The idea was to explore how web login systems handle authentication attempts and understand some of the security risks associated with weak password policies.

## What I Used

- **Python 3** – Main programming language.
- **Requests** – For sending HTTP requests and handling server responses.
- **Threading** – For managing shared resources and coordinating multiple threads.
- **ThreadPoolExecutor** – For experimenting with concurrent request handling.
- **File Handling** – For reading password lists from text files.

## What I Explored

- Understanding HTTP POST requests.
- Learning how web login forms handle submitted credentials.
- Working with cookies and HTTP sessions.
- Reading password lists from external text files.
- Using multithreading in Python.
- Understanding how server responses can indicate authentication success or failure.
- Exploring basic web authentication security concepts.

## Files

| **File** | **Description** |
|---|---|
| `login_tester.py` | Main Python script for the authentication testing experiment. |
| `requirements.txt` | Lists the external Python dependencies. |

## Things I Learned

This project helped me get a better understanding of:

- HTTP communication between clients and servers.
- How login forms process authentication requests.
- Python's Requests library.
- Multithreading and concurrent execution.
- Cookie handling in web applications.
- Some security risks associated with weak passwords and insufficient login protection.

## Current Limitations

There are still plenty of things I need to improve and understand better:

- Login failure detection depends on the response message.
- Different websites use different authentication mechanisms.
- No support for complex authentication flows.
- No proper handling of CSRF tokens.
- Limited error handling.
- Concurrent requests may be affected by server-side rate limiting.

## Disclaimer

This project was created for learning and educational purposes.

It should only be used against locally hosted test applications, systems you own, or environments where you have explicit permission to conduct security testing.

It is not intended for unauthorised account access.

---

**Author:** Pushkar

*Part of my ongoing journey into Python programming, cybersecurity, and ethical hacking.*
