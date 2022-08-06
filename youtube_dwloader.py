from pytube import YouTube
link = input("Enter the link for download: ")

yt = YouTube(link)
print("Title: ",yt.title)
yd = yt.streams.get_highest_resolution()
yd.download("/home/hasanfurkan/Downloads")
