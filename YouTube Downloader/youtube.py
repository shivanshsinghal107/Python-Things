import tkinter as tk
import pytube
from pytube import YouTube
import sys
import os

def progress_function(self, chunk, bytes_remaining):
    sys.stdout.write("\r")
    sys.stdout.write("{}% downloaded".format(round((1 - bytes_remaining/size)*100, 2)))
    sys.stdout.flush()

def download():
    global video_url
    global size
    print(f'Just a sec, fetching available resolutions for {yt.title}')
    url = video_url.get()
    yt = YouTube(str(url), on_progress_callback = progress_function)
#    try:
    videos = yt.streams.filter(progressive = True, file_extension = "mp4")

    count = 1
    for video in videos:
        size = video.filesize
        stream = str(video)
        res = stream.find('res') + 5
        print(f'{count}. {stream[res:res+4]} {round(size/1024**2, 2)} MB')
        count += 1
    choice = int(input('Enter the video number you want to download: '))
    req_video = videos[choice-1]
    destination = os.getcwd()
    req_video.download(destination)
    print(f'\n{yt.title} has been downloaded to {destination}.')
#    except:
#        print("This video can't be downloaded. Please try again later.")

root = tk.Tk()

canvas = tk.Canvas(root, height = 300, width = 750, bg = "white")
canvas.pack()

photo = tk.PhotoImage(file = 'yt_logo.png')
canvas.create_image(360, 140, image = photo)

heading = tk.Label(root, text = "YouTube Downloader", font = "arial 30 bold", fg = "#232529")
heading.pack()

widget = tk.Label(root, text = "Enter the Video URL:\n", font = "arial 14 italic", fg = "#232529")
widget.pack()

video_url = tk.Entry(root, width = 100)
video_url.pack()

space = tk.Label(root, text = "\n")
space.pack()

button = tk.Button(root, text = "Download", command = download, font = "arial 16 bold", fg = "white", bg = "red", bd = 0)
button.pack()

space = tk.Label(root, text = "\n")
space.pack()

root.mainloop()
