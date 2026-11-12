import requests
from concurrent.futures import ThreadPoolExecutor

target_url = input('enter the target url: ')
file_name = input('enter name of the file containing directories: ')
file = open(file_name, 'r')

# Define the HTTP status codes you want to filter for
VALID_STATUS_CODES = {200, 301, 302, 403, 401}

def request(url):
    try:
        # allow_redirects=False helps catch hidden redirects explicitly
        return requests.get('http://' + url, allow_redirects=False)
    except requests.exceptions.ConnectionError:
        pass

def check_path(line):
    dir = line.strip()
    if not dir or dir.startswith('#'):
        return
    full_url = target_url + '/' + dir
    response = request(full_url)
    
    # Filter response: Only print if response exists and status code is in our valid set
    if response and response.status_code in VALID_STATUS_CODES:
        print(f'discovered directory at the path: {full_url} [Status: {response.status_code}]')

# Run the file lines concurrently using 10 worker threads
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(check_path, file)

file.close()
