import requests
import time

url = "https://drscan-backend.onrender.com"

def send_request():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"GET request sent to {url} - Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending GET request to {url}: {e}")

def main():
    interval_minutes = 2
    interval_seconds = interval_minutes * 60

    while True:
        send_request()
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
