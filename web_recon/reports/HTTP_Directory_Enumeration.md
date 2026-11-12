# HTTP Directory Enumeration – Multithreaded Python Lab

## 1. Project Overview

This project documents a basic web directory enumeration exercise using a custom Python script.

The script uses HTTP requests and multithreading to check a list of commonly used directory names against a target web server. It identifies accessible paths and displays their HTTP response status codes.

The objective of this exercise was to understand how directory enumeration works, how HTTP status codes help identify resources, and how Python's ThreadPoolExecutor can improve the efficiency of repetitive network requests.

## 2. Objective

- Understand the basics of HTTP directory enumeration.
- Use a wordlist to check commonly used web directory paths.
- Identify paths returning selected HTTP status codes.
- Implement concurrent HTTP requests using Python.
- Understand how HTTP response codes help in basic web reconnaissance.

## 3. Tools and Technologies Used

- **Python 3** – Main programming language.
- **Requests** – Used to send HTTP GET requests and receive server responses.
- **Concurrent.futures** – Used for multithreading through ThreadPoolExecutor.
- **Directory Wordlist** – A text file containing directory names to check.
- **Target Web Server** – An authorized lab environment used for testing.

## 4. Working Methodology

The script follows a straightforward process:

1. Accepts the target URL from the user.
2. Accepts the path to a text file containing directory names.
3. Reads directory names from the supplied wordlist.
4. Creates a maximum of 10 worker threads.
5. Each worker checks a directory by sending an HTTP GET request.
6. Redirects are not automatically followed, allowing their original response codes to be observed.
7. Filters responses based on a predefined list of HTTP status codes.
8. Displays matching paths along with their corresponding status codes.

## 5. HTTP Status Codes

The script filters responses using the following status codes:

| Status Code | Meaning |
|---|---|
| 200 | OK – Resource successfully accessed |
| 301 | Moved Permanently – Permanent redirect |
| 302 | Found – Temporary redirect |
| 401 | Unauthorized – Authentication required |
| 403 | Forbidden – Access to the resource is denied |

These responses can provide useful information during web reconnaissance.

A 403 response, for example, does not necessarily mean that a directory contains accessible content. It simply indicates that the server refused the request.

## 6. Multithreading Implementation

The script uses Python's ThreadPoolExecutor from the concurrent.futures module.

A maximum of 10 worker threads are created:

`ThreadPoolExecutor(max_workers=10)`

This allows multiple directory checks to run concurrently instead of waiting for each request to finish before starting the next one.

Since HTTP requests involve network waiting time, multithreading can make this type of task more efficient.

## 7. Error Handling

The script includes basic exception handling for connection errors.

If a connection cannot be established, the request function returns without producing a response.

This prevents certain connection failures from interrupting the entire enumeration process.

## 8. Limitations

This is an introductory project and has several limitations:

- Only HTTP requests are used; HTTPS is not automatically handled.
- The script uses a fixed set of HTTP status codes.
- No request timeout has been configured.
- Only connection errors are explicitly handled.
- No response-size or content analysis is performed.
- The script does not distinguish between actual directories and application routes.
- The target URL must be supplied in a compatible format.
- The script does not include rate limiting or advanced request handling.

## 9. Learning Outcomes

Through this exercise, I gained practical experience with:

- Python HTTP requests using the Requests library.
- Reading and processing text-based wordlists.
- Understanding common HTTP response status codes.
- Using ThreadPoolExecutor for concurrent tasks.
- Basic exception handling in network-related scripts.
- Understanding the role of directory enumeration in web reconnaissance.

## 10. Conclusion

This project helped me understand the basic concept of HTTP directory enumeration and how it can be implemented using Python.

It was also a useful introduction to multithreading and handling multiple network requests concurrently.

Although the script is relatively simple, it provided practical experience with HTTP communication, response handling, wordlist processing, and basic web reconnaissance techniques.

**Note:** This tool was developed for educational purposes and should only be tested against systems where explicit authorization has been granted.
