import pytube

youtube = pytube.YouTube('https://youtu.be/mYFbLFYpGuE')
video = youtube.streams.filter(progressive=True).desc().first()
video = youtube.streams.get_by_itag(137)

video.download()

youtube.title
youtube.length
youtube.views