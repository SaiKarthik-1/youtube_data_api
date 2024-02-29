import logging
import sys
import requests
import json
import logging
from requests.auth import HTTPBasicAuth


def verify_channel(channel_name):
    api_key = "AIzaSyAJ2Tg7hzHftPVKqnspAYL62GUgfP-qNa8"
    URL = f"https://www.googleapis.com/youtube/v3/channels?key={api_key}&forUsername={channel_name}&part=statistics"
    r = requests.get(url = URL)
    data = r.json()
    data = json.dumps(data,indent=2)
    print(f"For Channel {channel_name}, the statistics are:")
    print(data)