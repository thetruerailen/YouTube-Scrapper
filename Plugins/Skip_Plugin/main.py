from pytube import YouTube
import os

url = input("What is the url? : ")

def download_360p_mp4_videos(url: str, outpath: str = "./"):

    yt = YouTube(url)

    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)


if __name__ == "__main__":

    download_360p_mp4_videos(
        "https://www.youtube.com/watch?v=Dg0IjOzopYU",
        "./Music",
    )