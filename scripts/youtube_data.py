import logging
import sys
import requests
import json
import logging
from requests.auth import HTTPBasicAuth

from scripts.youtube_api import get_data_from_api

api_key = "AIzaSyAJ2Tg7hzHftPVKqnspAYL62GUgfP-qNa8"
def verify_channel(data):
    if 'https' in data:
        if 'watch' in data:
            analyse_video(data)
        else:
            call_channel_link_api(data)
    else:
        analyse_channel(data)


def analyse_video(video_id):

    video_stats = get_video_data(video_id, 'statistics')

    video_snippet = get_video_data(video_id, 'snippet')
    channel_id = video_snippet['items'][0]['snippet']['channelId']

    channel_data = get_channel_data({'id':channel_id}, 'statistics')


    data_analyser(channel_data, video_stats)


def call_channel_link_api(channel_link):
    return channel_link

def analyse_channel(channel_name):
    params = {'forUsername':{channel_name}}
    channel_data = get_channel_data(params, 'statistics')

    channel_snippet = get_channel_data(params, 'snippet')
    print(channel_snippet)

def get_video_data(video_id, part):
    type = 'videos'
    video_id = video_id[-11:]
    params = {'key': {api_key}, 'id': {video_id}, 'part': {part}}
    data = get_data_from_api(type, params)
    return data


def get_channel_data(params, part):
    type = 'channels'
    local_params = {'part':part,'key':api_key}
    params.update(local_params)
    data = get_data_from_api(type, params)
    return data


def data_analyser(channel_data, video_data):
    total_subscriber_count = int(channel_data['items'][0]['statistics']['subscriberCount'])
    total_view_count = int(channel_data['items'][0]['statistics']['viewCount'])
    total_number_of_videos = int(channel_data['items'][0]['statistics']['videoCount'])
    print('CHANNEL DETAILS')
    print(f'Subscriber Count: {total_subscriber_count}')
    print(f'View Count: {total_view_count}')
    print(f'Number of videos: {total_number_of_videos}')
    engagement_rate = ((total_view_count/total_number_of_videos)/total_subscriber_count)*100
    print(f'Total Viewrship Percentage (By subscriber count) : {engagement_rate} %')

    video_view_count = int(video_data['items'][0]['statistics']['viewCount'])
    video_like_count = int(video_data['items'][0]['statistics']['likeCount'])
    video_comment_count = int(video_data['items'][0]['statistics']['commentCount'])

    print('\nVIDEO STATISTICS')
    print(f'Total Number of views: {video_view_count}')
    print(f'Total Number of likes for video: {video_like_count}')
    print(f'Total Number of comments for video: {video_comment_count}')

    viewership_percentage = (video_view_count/total_subscriber_count) * 100
    likes_percentage = (video_like_count/total_subscriber_count) * 100

    print(f'Viewership Percentage for the video : {viewership_percentage} %')
    print(f'Likes Percentage for the video: {likes_percentage} %')