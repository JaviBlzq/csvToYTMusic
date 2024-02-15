import menu
import handlerAPI
from youtube_api import YouTubeDataAPI

if __name__ == '__main__':
    # Choose the csv and get ready to work with it.
    tracks = menu.get_data()
    #print(tracks.head())
    song = tracks.loc[1,]
    song = song['Track name']+ ' - ' + song['Artist name']
    print(song)
    videoId = handlerAPI.getVideoId(song)
    handlerAPI.insertVideo(videoId)
