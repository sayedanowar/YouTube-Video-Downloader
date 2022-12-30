
from pytube import YouTube, Playlist, Search
import urllib.request

def is_connected():
  try:
    urllib.request.urlopen("https://www.google.com", timeout=5)
    return True
  except urllib.request.URLError:
    return False

if is_connected():
    print("\n>> YouTube VIDEO DOWNLOADER <<\n")
    yt_data = int(input("1. Download Single Video/Audio\n2. Download Playlist Video/Audio\n3. Search Video\n\n>> "))

    if yt_data == 1:
        video_link = input("\nEnter Video URL :\n\n>> ")

        if video_link.startswith('https://www.youtube.com/') or video_link.startswith('https://youtu.be/') or video_link.startswith('https://youtube.com/'):
        
            youtube = YouTube(video_link)

            print("\nVideo Details :\n")
            print("Title        : ", youtube.title)
            print("Author       : ", youtube.author)
            print("Channel      : ", youtube.channel_url)
            print("Publish Date : ", youtube.publish_date)
            print("Views        : ", youtube.views)

            download_format = int(input("\nIn Which Format You Want To Download :\n1. Video\n2. Audio\n\n>> "))

            if  download_format == 1:
                resolution = int(input("\nResolution :\n1. High\n2. Low\n\n>> "))
                if resolution == 1:
                    print("\nDownloading...")
                    yt_video = youtube.streams.get_highest_resolution().download()
                    print("\nDownloaded Successfully\n")
                elif resolution == 2:
                    print("\nDownloading...")
                    yt_video = youtube.streams.get_lowest_resolution().download()
                    print("\nDownloaded Successfully\n")
                else:
                    print("\nInput Not Found\n")

            elif download_format == 2:
                print("\nDownloading...")
                yt_audio = youtube.streams.get_audio_only().download()
                print("\nDownloaded Successfully\n")

            else:
                print("\nInput Not Found\n")

        else:
            print("\nEnter YouTube Video Link Only\n")

    elif yt_data == 2:
        playlist_link = input("\nEnter Playlist Link :\n\n>> ")

        if playlist_link.startswith('https://www.youtube.com/') or playlist_link.startswith('https://youtube.com/'):
        
            playlist_videos = Playlist(playlist_link)

            print("\nPlayList Details :\n")
            print(f"Title   : {playlist_videos.title}")
            print(f"Author  : {playlist_videos.owner}")
            print(f"Videos  : {playlist_videos.length}")

            download_format = int(input("\nDownload PlayList :\n1. Video\n2. Audio\n\n>> "))

            if  download_format == 1:
                video_quality = int(input("\nVideo Quality :\n1. High\n2. Low\n\n>> "))
                if video_quality == 1:
                    print("\nDownloading...")
                    for video in playlist_videos.videos:
                        video.streams.get_highest_resolution().download()
                    print("\nDownloaded Successfully\n")

                elif video_quality == 2:
                    print("\nDownloading...")
                    for video in playlist_videos.videos:
                        video.streams.get_lowest_resolution().download()
                    print("\nDownloaded Successfully\n")

                else:
                    print("\nInput Not Found\n")

            elif download_format == 2:
                print("\nDownloading...")
                for audio in playlist_videos.videos:
                    audio.streams.get_audio_only().download()
                print("\nDownloaded Successfully\n")

            else:
                print("\nInput Not Found\n")

        else:
            print("\nEnter YouTube PlayList Link Only\n")

    elif yt_data == 3:
        keyword = input("\nSearch YouTube :\n\n>> ")

        search = Search(keyword)

        print("")
        for data in search.results:
            print(f"Title  : {data.title}\nAuthor : {data.author}\nLink   : {data.watch_url}\n")

else:
    print("\nPlease Check Your Internet Connection!\n")