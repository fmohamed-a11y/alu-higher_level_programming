#!/usr/bin/python3
"""Send a request and display the X-Request-Id header value."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
