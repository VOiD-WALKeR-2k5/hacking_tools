# Email Scraper

A beginner Python web scraping project that extracts email addresses found in webpage source code.

The script starts with a user-provided URL, visits discovered links, searches webpage content for email addresses using regular expressions, and displays the collected results.

This project was created as a learning exercise to understand web scraping, HTML parsing, URL handling, and basic crawling techniques using Python.

## Features

- Accepts a target URL through user input.
- Fetches webpage content using HTTP GET requests.
- Parses HTML using BeautifulSoup.
- Extracts email addresses using regular expressions.
- Discovers links from HTML anchor tags.
- Uses a queue to manage URLs waiting to be processed.
- Uses sets to avoid duplicate URLs and email addresses.
- Limits processing to a maximum of 100 URL iterations.
- Handles basic connection errors and keyboard interruption.

## Requirements

- Python 3
- Requests
- BeautifulSoup4
- lxml

## Installation

Clone the repository:

```bash
git clone https://github.com/VOiD-WALKeR-2k5/hacking_tools.git
```

Navigate to the project directory:

```bash
cd hacking_tools/tools/Email_Scraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python email_scraper.py
```

Enter the target URL when prompted:

```text
[+] Enter Target URL To Scan: https://example.com
```

The script will begin processing webpages and display discovered email addresses.

Example output:

```text
[1] Processing https://example.com
[2] Processing https://example.com/contact
[3] Processing https://example.com/about

contact@example.com
info@example.com
```

*Example output is illustrative, not a verified execution result.*

## How It Works

1. Takes a starting URL from the user.
2. Adds the URL to a queue.
3. Retrieves webpage content.
4. Searches the response text for email addresses.
5. Parses HTML and discovers links.
6. Adds discovered URLs to the processing queue.
7. Continues until the queue is empty or the processing limit is reached.
8. Prints the collected email addresses.

## Limitations

- Processes a maximum of 100 URL iterations.
- Does not restrict discovered links to the original domain.
- Does not include configurable request timeouts.
- Uses a basic regular expression for email extraction.
- Does not handle every possible URL format.
- Does not save results to an external file.
- Does not guarantee that extracted email addresses are valid or active.
- Does not handle JavaScript-rendered webpage content.

## Disclaimer

This project is intended for educational purposes and authorized web reconnaissance only.

Only use it on websites where you have permission to perform testing. Respect website terms, privacy requirements, and applicable data protection laws. Do not use it to harvest personal contact information or build unsolicited mailing lists.
