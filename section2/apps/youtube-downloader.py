import pytube
import os
import subprocess


yt = pytube.YouTube("https://www.youtube.com/watch?v=33WeMjZghoQ&t=4s")

videos = yt.streams

# print('videos', videos)

for i in range(len(videos)):
    print(i, ', ', videos[i])


cNum = int(input("Choose the resolution you want to download:"))

down_dir = "C:\\Users\\yongs\\Documents\\youtube"

videos[cNum].download(down_dir)

newFileName = input("Input the new name for MP3 file:")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
                 os.path.join(down_dir, oriFileName),
                 os.path.join(down_dir, newFileName)
])


print("Youtube video download complete and converstion is done.")

