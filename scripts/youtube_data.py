import logging
import sys
import requests
import json
import logging
from requests.auth import HTTPBasicAuth

from scripts.youtube_api import get_channel_data, get_video_data, get_video_from_channel_name


def process_data(data):
    if 'https' and 'watch' in data:
        data_analyser(data) # this is a video link
    else:
        analyse_channel(data)


def analyse_channel(channel_name):
    if 'https' in channel_name:
        print()
    else:
        video_id = get_video_from_channel_name(channel_name)
    data_analyser(video_id)


def data_analyser(video_id):
    video_snippet = get_video_data(video_id, 'snippet')        # getting channel_id
    channel_id = video_snippet['items'][0]['snippet']['channelId']

    video_data = get_video_data(video_id, 'statistics') # getting video statistics
    channel_data = get_channel_data(channel_id, 'statistics')  # getting channel_data

    channel_snippet = get_channel_data(channel_id, 'snippet')

    video_title = video_snippet['items'][0]['snippet']['title']
    channel_title = channel_snippet['items'][0]['snippet']['title']

    print_analysed_data(channel_data, video_data, channel_title, video_title)

def print_analysed_data(channel_data, video_data, channel_title, video_title):
    total_subscriber_count = int(channel_data['items'][0]['statistics']['subscriberCount'])
    total_view_count = int(channel_data['items'][0]['statistics']['viewCount'])
    total_number_of_videos = int(channel_data['items'][0]['statistics']['videoCount'])
    print(f'CHANNEL DETAILS FOR CHANNEL: {channel_title}')
    print(f'Subscriber Count: {total_subscriber_count}')
    print(f'View Count: {total_view_count}')
    print(f'Number of videos: {total_number_of_videos}')
    engagement_rate = ((total_view_count/total_number_of_videos)/total_subscriber_count)*100
    print(f'Total Viewrship Percentage (By subscriber count) : {engagement_rate} %')

    video_view_count = int(video_data['items'][0]['statistics']['viewCount'])
    video_like_count = int(video_data['items'][0]['statistics']['likeCount'])
    video_comment_count = int(video_data['items'][0]['statistics']['commentCount'])

    print(f'\nVIDEO STATISTICS FOR VIDEO: {video_title}')
    print(f'Total Number of views: {video_view_count}')
    print(f'Total Number of likes for video: {video_like_count}')
    print(f'Total Number of comments for video: {video_comment_count}')

    viewership_percentage = (video_view_count/total_subscriber_count) * 100
    likes_percentage = (video_like_count/total_subscriber_count) * 100

    print(f'Viewership Percentage for the video : {viewership_percentage} %')
    print(f'Likes Percentage for the video: {likes_percentage} %')