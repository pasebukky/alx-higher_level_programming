#!/usr/bin/python3

"""
    Python script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
