import os 

local = "./Users/gabgu/Desktop/MessyFolder"


def createFolders():

    files = os.listdir("C:/Users/gabgu/Desktop/MessyFolder")
    typesFiles = []

    for i in range(len(files)):
        x = files[i].split(".")
        typesFiles.append(x[-1])
    

    print(typesFiles)


createFolders()