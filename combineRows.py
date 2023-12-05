import os
import pathlib

folderName = input("What is the name of the folder containing the files: ")

currentDir = str(pathlib.Path(__file__).parent.resolve())
fullFolderPath = currentDir + "/" + folderName + "/"

if not os.path.isdir(fullFolderPath):
    print("That folder does not exist")
    quit()

folderDir = os.listdir(fullFolderPath)
fileNumInFolder = len(folderDir)

try:
    newFile = open(fullFolderPath + "All " + folderName + ".txt", "x")
except FileExistsError:
    print("File already exists")
    quit()

for i in folderDir:
    readFile = open(fullFolderPath + i, "r")
    fileData = readFile.readlines()
    newFile.writelines(fileData)
    newFile.writelines("\n")
    readFile.close()
    
newFile.close()
print("file created")