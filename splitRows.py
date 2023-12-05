import math
import os
import pathlib

fileName = input("What is the filename (excluding .txt): ")
rowCount = int(input("How many rows per file: "))
fileNum = 0
currentDir = str(pathlib.Path(__file__).parent.resolve())
fullFolderPath = currentDir + "/" + fileName + "/"

readFile = open(currentDir + "/" + fileName + ".txt", "r")

fileData = readFile.readlines()

if not os.path.isdir(fullFolderPath):
    os.mkdir(fullFolderPath)

numberOfFiles = math.ceil(len(fileData)/rowCount)

for i in range(1, numberOfFiles + 1):
    try:
        newFile = open(fullFolderPath + str(fileNum) + fileName + ".txt", "x")
        newFile.writelines(fileData[0 + (rowCount * (i-1)):(rowCount * i)])
        newFile.close()
    except FileExistsError:
        print("File already exists")
        break

    fileNum += 1

readFile.close()
print(str(numberOfFiles) + " files created")