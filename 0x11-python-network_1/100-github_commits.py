#!/usr/bin/python3
"""
This script show the list of 10 commits
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    repo = argv[1]
    owner = argv[2]
    rq = requests.get(url.format(owner, repo))
    commit = rq.json()
    for committ in commit[:10]:
        print(committ.get('sha'), end=': ')
        print(committ.get('commit').get('author').get('name'))
