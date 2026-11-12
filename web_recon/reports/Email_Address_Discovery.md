# Email Address Discovery Using Python – Web Reconnaissance Lab

## 1. Project Overview

This project documents a basic email address discovery exercise using a custom Python web scraping script.

The script visits webpages starting from a user-provided URL, extracts email addresses from the retrieved HTML content, and identifies additional links to process.

The project was developed to understand the fundamentals of web scraping, HTML parsing, URL handling, and automated information gathering.

## 2. Objectives

- Understand the fundamentals of web scraping.
- Learn how to retrieve webpage content using Python.
- Extract email address patterns using regular expressions.
- Understand HTML parsing with BeautifulSoup.
- Explore URL discovery and queue-based crawling.
- Learn how Python sets can prevent duplicate entries.
- Understand basic exception handling in network requests.

## 3. Tools and Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3 | Main programming language |
| Requests | Retrieving webpage content |
| BeautifulSoup | Parsing HTML documents |
| lxml | HTML parsing backend |
| Regular Expressions | Identifying email address patterns |
| Collections.deque | Maintaining the URL processing queue |

## 4. Working Methodology

The script follows a basic crawling and extraction process.

1. Accepts a starting URL from the user.
2. Initializes a queue containing the starting URL.
3. Retrieves URLs from the queue one at a time.
4. Sends HTTP GET requests to retrieve webpage content.
5. Searches the response text for email address patterns using regular expressions.
6. Stores discovered email addresses in a set to avoid duplicates.
7. Parses the webpage using BeautifulSoup.
8. Extracts links from HTML anchor tags.
9. Adds newly discovered links to the processing queue.
10. Repeats the process until the queue is empty or the processing limit is reached.
11. Displays the collected email addresses.

## 5. Email Extraction

The script uses Python's regular expression module to identify strings matching a basic email address pattern.

The extracted addresses are stored in a Python set.

Using a set helps prevent the same email address from appearing multiple times in the final results.

It is important to understand that matching an email pattern does not confirm that the address exists or is active.

## 6. URL Crawling and Queue Management

The script uses `collections.deque` to maintain a queue of URLs waiting to be processed.

It also maintains two sets:

- `scraped_urls`: Stores URLs that have already been processed.
- `emails`: Stores discovered email addresses.

This helps avoid repeatedly processing URLs that have already been visited and prevents duplicate email entries.

The script also includes a processing limit of approximately 100 URL iterations.

## 7. Error Handling

Basic exception handling is implemented using the Requests library.

The script handles:

- Missing URL schema errors.
- Connection errors.
- Keyboard interruption.

When a connection error occurs, the script skips that URL and continues processing the remaining queue.

## 8. Observations

During this exercise, the following concepts were explored:

- Retrieving HTML content from websites.
- Extracting information from webpage source code.
- Identifying email patterns using regular expressions.
- Discovering links through HTML anchor tags.
- Managing URLs using queue-based processing.
- Avoiding duplicate results using Python sets.

Actual findings and screenshots should be added after running the script in an authorized test environment.

## 9. Limitations

The current implementation has several limitations:

- The script does not restrict crawling to the original website's domain.
- A maximum of 100 URL iterations is allowed.
- No request timeout is configured.
- The email extraction pattern is basic and may miss certain valid formats.
- Extracted addresses are not verified.
- JavaScript-generated content is not processed.
- URL normalization and relative-link handling are basic.
- The script does not export results into a file.
- HTTP response status codes are not explicitly checked.

## 10. Learning Outcomes

Through this exercise, I gained practical experience with:

- Python Requests for retrieving webpage content.
- BeautifulSoup for HTML parsing.
- Regular expressions for pattern matching.
- URL handling using urllib.parse.
- Queue-based crawling using deque.
- Managing duplicate data using sets.
- Basic exception handling in web scraping.

## 11. Conclusion

This project provided a practical introduction to web scraping and basic web reconnaissance using Python.

It helped me understand how webpages can be retrieved, parsed, and searched for specific information using Python libraries.

It also introduced me to basic crawling techniques and data structures that can be used when developing simple web scraping utilities.

**Disclaimer:** This project is intended for educational purposes and authorized testing only. Any collection or processing of contact information should respect website permissions, privacy requirements, and applicable data protection laws.
