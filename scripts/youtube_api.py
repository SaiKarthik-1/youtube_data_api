import requests
import json


def get_data_from_api(type, params):
    URL = f"https://www.googleapis.com/youtube/v3/{type}"
    r = requests.get(url=URL, params= params)
    data = r.json()
    return data