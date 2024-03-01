#!/usr/bin/python3

"""
    Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

import sys
import requests


if __name__ == "__main__":
    username = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=username)
    print(response.json().get("id"))
