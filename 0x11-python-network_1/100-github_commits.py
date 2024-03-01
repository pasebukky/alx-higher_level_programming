#!/usr/bin/python3

"""
    Write a Python script that lists the 10 recent
    commits on a given GitHub repository
"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits" \
          .format(owner, repo)

    response = requests.get(url)
    commits = response.json()

    try:
        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
