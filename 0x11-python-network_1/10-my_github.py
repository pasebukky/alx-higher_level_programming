#!/usr/bin/python3

"""
    Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    verification = HTTPBasicAuth(username, token)
    response = requests.get(url, auth=verification)
    print(response.json().get("id"))
