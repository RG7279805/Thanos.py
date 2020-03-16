import os
import random
import math
dirfiles = os.listdir()
totalFiles = len(dirfiles)

def delete(file):
    os.remove(file)


x = 0
while x < totalFiles/2:
    FilesLeft = os.listdir()
    print(FilesLeft)
    numberOfFilesLeft = len(FilesLeft) -1
    print(numberOfFilesLeft,'number of files left')
    randomInt = random.randint(1,numberOfFilesLeft) -1
    print('random int =',randomInt)
    print('file to bo deleted',dirfiles[random.randint(0,numberOfFilesLeft)])
    if FilesLeft[randomInt] == 'thanos.py':
        pass
    else:
        delete(FilesLeft[randomInt])
    x+=1
