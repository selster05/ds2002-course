#!/usr/bin/env python3

# importing libraries
import os
import json
import requests

# Get GH username
GHUSER = os.getenv("GITHUB_USER")

print("GHUSER =", GHUSER)

# GH API url
url = f'https://api.github.com/users/{GHUSER}/events'

# Fetching recent activity
r = json.loads(requests.get(url).text)

print(r)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)


