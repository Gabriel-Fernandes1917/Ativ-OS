import os 
import shutil as sh

local = "C:/Users/gabgu/Desktop/MessyFolder"

def messy():
    global files
    files = os.listdir(local)

    for i in range(0, len(files)):
        folders = files[i]
        
        if len(folders.split(".")) == 1:
 
            folder = local+"/"+files[i]
            filesInFolder = os.listdir(folder)
            for x in range(0, len(filesInFolder)):
                sh.move(folder+"/"+filesInFolder[x], local)

    for i in range(0, len(files)):
        os.rmdir(local+"/"+files[i])

messy()