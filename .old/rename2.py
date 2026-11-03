import os

root = "D:/Headway_Beginner_5e/Struct/Media/Student's Book"

for dir in os.listdir(root):
    directory = os.path.join(root, dir)
    if os.path.isdir(directory):
        n = 1
        for f in os.listdir(directory):
            file = os.path.join(directory, f)
            os.rename(file, os.path.join(directory, f"{str(n).zfill(2)}.mp3"))
            n+=1