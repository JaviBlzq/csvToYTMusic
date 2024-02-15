import menu
import handlerAPI


if __name__ == '__main__':
    # Choose the csv and get ready to work with it.
    tracks = menu.get_data()
    for i in range(len(tracks)):
        song = tracks.loc[i,]
        song = song['Track name']+ ' - ' + song['Artist name']
        print(str(i) + ":" + song)
        videoId = handlerAPI.getVideoId(song)
        handlerAPI.insertVideo(videoId)
