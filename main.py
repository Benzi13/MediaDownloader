from pytube import YouTube, Playlist
import os

MP4_SUFFIX = ".mp4"
MP3_SUFFIX = ".mp3"
MATCH_SUFFIX = {True: MP3_SUFFIX,
                False: MP4_SUFFIX}

def handle_single_download(link: str, only_audio: bool):
    youtubeObject = YouTube(link)
    single_download(youtubeObject, only_audio)


def handle_playlist(link: str, only_audio: bool):
    playlist = Playlist(link)
    print(f'Downloading: {playlist.title}')
    for video in playlist.videos:
        single_download(video, only_audio)
        
def single_download(pytube_object, only_audio: bool):
    if only_audio:
        video_holder = pytube_object.streams.filter(only_audio=only_audio).first()
    else:
        video_holder = pytube_object.streams.get_highest_resolution()
    try:
        out_file = video_holder.download()
    except Exception as e:
        print(f"Got exception:{e}")
    change_suffix(out_file, MATCH_SUFFIX[only_audio])
    print("Download is completed successfully")

def change_suffix(file_name: str, new_filename: str):
    base, ext = os.path.splitext(file_name)
    base = base.split("-")[1]
    new_filename = base + new_filename
    os.rename(file_name, new_filename)
    

def main():
    while True:
        link = input("Enter the YouTube Link: ")
        choice = input("What do you want to do with that link?\n1. Download Video.\n2. Download Song.\n3. Download Playlist of Videos.\n4.Download a Playlist of Songs")
        if choice == "1":
            handle_single_download(link, False)
        if choice == "2":
            handle_single_download(link, True)
        elif choice == "3":
            handle_playlist(link, False)
        elif choice == "4":
            handle_playlist(link, True)

if __name__ == "__main__":
    main()