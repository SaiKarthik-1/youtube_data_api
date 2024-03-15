import requests

api_key = "AIzaSyAJ2Tg7hzHftPVKqnspAYL62GUgfP-qNa8"


def get_data_from_api(type, params):
    """
    Fetches the data from youtube API by making an API call
    :param type: Specifies what type of API call is being made (channel, video or search)
    :param params: Input parameters for the API call
    :return: returns the response data in a JSON format
    """

    try:
        URL = f"https://www.googleapis.com/youtube/v3/{type}"
        r = requests.get(url=URL, params=params)
        data = r.json()
        return data
    except Exception as e:
        print(f'Exception ocurred during API call : {e}')


def get_video_data(video_id, part):
    """
    getting video data using youtube video api
    :param video_id: The link or id of a particular youtube video
    :param part: specifies if we want statistics or snippet of the data
    :return: Returns video data
    """

    type = 'videos'
    video_id = video_id[-11:]
    params = {'key': {api_key}, 'id': {video_id}, 'part': {part}}
    data = get_data_from_api(type, params)
    return data


def get_channel_data(channel_id, part):
    """
    getting channel data using youtube channel api
    :param channel_id: Channel ID of a particular youtube channel
    :param part: specifies if we want statistics or snippet of the data
    :return: Returns channel data
    """

    type = 'channels'
    params = {'id': channel_id, 'part': part, 'key': api_key}
    data = get_data_from_api(type, params)
    return data


def get_videoid_from_channel_name(channel_name):
    """
    Fetches the latest video id from a particular channel
    :param channel_name: Channel name of a particular YouTube channel
    :return: Returns the latest video id
    """

    try:
        # getting channel data using youtube search api
        type = 'search'
        params = {'part': 'snippet', 'key': api_key, 'type': 'channel', 'q': f'{channel_name}'}
        channel_data = get_data_from_api(type, params)

        # checking if the channel exists or not
        results_flag = channel_data['pageInfo']['totalResults']
        if results_flag == 0:
            exit('Not a valid youtube channel for the API')

        # if exists, getting channel id
        channel_id = channel_data['items'][0]['id']['channelId']

        # taking input from user if shorts needs to be included or not
        shorts_flag = input(f'Should shorts be included in the results of {channel_name} ? (\'True\' or \'False\'): ')

        # getting video data from video API
        params = {'part': 'snippet', 'key': api_key, 'type': 'video', 'channelId': {channel_id}, 'order': 'date'}
        video_data = get_data_from_api(type, params)

        # getting the latest video id including shorts
        if shorts_flag == 'True' or shorts_flag == 'true':
            video_id = video_data['items'][0]['id']['videoId']
        # getting the latest video id excluding shorts
        else:
            for i in range(5):
                if video_data['items'][i]['snippet']['description'] != '':
                    video_id = video_data['items'][i]['id']['videoId']
                    break
            else:
                exit('The latest 5 videos are shorts')

        return video_id

    except Exception as e:
        print(f'Exception ocurred while getting video id for channel - {channel_name} : {e}')