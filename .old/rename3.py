import os

root = "D:/Headway_Beginner_5e/Media/Videos"

for dir in os.listdir(root):
    directory = os.path.join(root, dir)
    if os.path.isdir(directory):
        for f in os.listdir(directory):
            file = os.path.join(directory, f)
            if "opener" in f:
                os.rename(file, os.path.join(directory, "Opener.mp4"))
            else:
                newName = f[f.rfind("Unit_")+8:].replace("_", " ")
                os.rename(file, os.path.join(directory, newName))