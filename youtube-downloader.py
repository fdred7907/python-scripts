import pytube

link = input("Youtube Video URL")

video_download = pytube.YouTube(link)

video_download.streams.first().download()

print("Video Downloaded",link)

