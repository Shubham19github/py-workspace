import os

path = "C:\\Users\\....."   #path of folder containing images
a = []

os.chdir(path)
a =os.listdir()

for x in range(len(a)):
    print(a[x])
