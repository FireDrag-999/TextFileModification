import os
import pathlib

folderName = input("What is the name of the folder containing the files: ") # script must be placed outside of the folder e.g. script, "records folder" in the same folder
                                                                            # All text files in a folder are combined in the order stored in the folder                                                                  
currentDir = str(pathlib.Path(__file__).parent.resolve())                   # Creates a file inside the folder called "!All (foldername).txt"   
fullFolderPath = currentDir + "/" + folderName + "/"                        # To run again the "!All (foldername).txt" file must be moved/deleted from the folder

if not os.path.isdir(fullFolderPath):
    print("That folder does not exist")
    quit()

folderDir = os.listdir(fullFolderPath)
fileNumInFolder = len(folderDir)

try:
    newFile = open(fullFolderPath + "!All " + folderName + ".txt", "x")
except FileExistsError:
    print("File already exists, delete !All " + folderName + ".txt from the folder")
    quit()

for file in folderDir:
    readFile = open(fullFolderPath + file, "r")
    fileData = readFile.readlines()
    newFile.writelines(fileData)
    #newFile.writelines("\n") # this is not needed if the rows already exported have a break line code as it will cause an extra line to appear
    readFile.close()
    
newFile.close()
print("file created")
