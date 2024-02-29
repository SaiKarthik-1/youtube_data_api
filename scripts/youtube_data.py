import logging
import sys
import requests
import json
import logging
from requests.auth import HTTPBasicAuth

api_key = "AIzaSyAJ2Tg7hzHftPVKqnspAYL62GUgfP-qNa8"
def verify_channel(data):
    if 'https' in data:
        if 'watch' in data:
            data = call_video_api(data)
        else:
            data = call_channel_link_api(data)
    else:
        data = call_channel_name_api(data)


def call_video_api(video_id):
    video_id = video_id[-11:]
    URL = f"https://www.googleapis.com/youtube/v3/videos?key={api_key}&id={video_id}&part=statistics"
    r = requests.get(url=URL)
    data = r.json()
    data = json.dumps(data, indent=2)
    print(f"For the given video, the statistics are:")
    print(data)

def call_channel_link_api(channel_link):
    print(channel_link)

def call_channel_name_api(channel_name):
    URL = f"https://www.googleapis.com/youtube/v3/channels?key={api_key}&forUsername={channel_name}&part=statistics"
    r = requests.get(url=URL)
    data = r.json()
    data = json.dumps(data, indent=2)
    print(f"For Channel {channel_name}, the statistics are:")
    print(data)