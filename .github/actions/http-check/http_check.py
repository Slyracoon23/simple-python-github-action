# .github/actions/http-check/http_check.py

import requests
import sys

def check_response(url):
    response = requests.get(url)
    print(response)
    if 'success' in response.text:
        print("Test Passed")
    else:
        print("Test Failed:", response.text)
        sys.exit(1)

if __name__ == "__main__":
    url = sys.argv[1]
    check_response(url)
