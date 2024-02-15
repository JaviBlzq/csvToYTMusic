# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtubepartner","https://www.googleapis.com/auth/youtube","https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "data/client_secret_1071491351317-u9il9g0o7a8gegqpt3816cunpdmubhbk.apps.googleusercontent.com.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_local_server(port=0)
youtube = googleapiclient.discovery.build(
api_service_name, api_version, credentials=credentials)
DEVELOPER_KEY = "AIzaSyCcBWFuViLXl87k1kEqiUN_HCK3w1TrnSs"

def getVideoId(songToSearch):
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=songToSearch
    )
    response = request.execute()

    return response['items'][0]['id']['videoId']

def insertVideo(videoId):
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": "PLjtL2zME1BQ0uAaIBylnF5ePFn0LWWbkd",
                "position": 0,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": videoId
                }
            }
        }
    )
    response = request.execute()

    print(response)