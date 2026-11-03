import os
print(os.path.abspath(os.getcwd()))
if input("Continue? Y/N:").lower() != "y":
    exit()

'''
root = "./"
for dir in os.listdir(root):
    if not os.path.isdir(os.path.join(root, dir)):
        continue
    for file in os.listdir(os.path.join(root, dir)):
        os.rename(os.path.join(root, dir, file), os.path.join(root, dir, file[-6:]))
        
'''

def printDir(dir):
    if dir[-4:] == ".git":
        return
    if os.path.isdir(dir):
        for subDir in os.listdir(dir):
            printDir(os.path.join(dir, subDir))
    else:
        print(dir)
printDir("./")
#'''


input("Finished! ")