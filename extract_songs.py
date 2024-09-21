import pandas as pd
import sys

_path = sys.argv[1]

data_list = pd.read_csv(_path)

titles = data_list["Title"]
albums = data_list["Album"]
lyrics = data_list["Lyrics"]

ordered_album = {}
for i in range(len(albums)):
    if(albums[i] not in ordered_album): ordered_album[albums[i]] = []
    ordered_album[albums[i]].append(titles[i].replace(" (Taylor's Version)", "").replace("'", ""))
print(ordered_album)

def toArr(_arr):
    to_write = ''
    for i in range(len(_arr)):
        to_write += f'"{_arr[i]}"'
        if(i < len(_arr) - 1): to_write += ","
    return f'[{to_write}]'

with open("titles.txt", "w") as f:
    f.write(toArr(titles))

with open("albums.txt", "w") as f:
    f.write(toArr(albums))

with open("lyrics.txt", "w") as f:
    f.write(toArr(lyrics))

print("Done")
