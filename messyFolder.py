import os 

local = "./Users/gabgu/Desktop/MessyFolder"


def createFolders():

    files = os.listdir("C:/Users/gabgu/Desktop/MessyFolder")
    typesFiles = []

    for i in range(len(files)):
        x = files[i].split(".")

        for i in range(len(files)):
            
            if i != x[-1]:
                typesFiles.append(x[-1])
    

    print(typesFiles)

    # for i in range(len(files)):



createFolders()