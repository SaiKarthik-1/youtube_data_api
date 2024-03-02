import requests
import json

api_key = "AIzaSyAJ2Tg7hzHftPVKqnspAYL62GUgfP-qNa8"
def get_data_from_api(type, params):
    URL = f"https://www.googleapis.com/youtube/v3/{type}"
    r = requests.get(url=URL, params= params)
    data = r.json()
    return data


def get_video_data(video_id, part):
    type = 'videos'
    video_id = video_id[-11:]
    params = {'key': {api_key}, 'id': {video_id}, 'part': {part}}
    data = get_data_from_api(type, params)
    return data


def get_channel_data(channel_id, part):
    type = 'channels'
    params = {'id':channel_id,'part':part,'key':api_key}
    data = get_data_from_api(type, params)
    return data


def get_video_from_channel_name(channel_name):
    shorts_flag = input('Should shorts be included in the results ? (\'True\' or \'False\'): ')
    type = 'search'
    params = {'part': 'snippet', 'key': api_key, 'type':'channel', 'q':f'{channel_name}'}
    channel_data = get_data_from_api(type, params)
    channel_id = channel_data['items'][0]['id']['channelId']

    params = {'part': 'snippet', 'key': api_key, 'type':'video', 'channelId':{channel_id}, 'order': 'date'}
    video_data = get_data_from_api(type, params)
    if shorts_flag == 'True' or shorts_flag == 'true':
        video_id = video_data['items'][0]['id']['videoId']
    else:
        for i in range(0,5):
            if video_data['items'][i]['snippet']['description'] != '':
                video_id = video_data['items'][i]['id']['videoId']
                break


    return video_id

