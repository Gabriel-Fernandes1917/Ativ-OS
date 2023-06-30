import os 
import shutil as sh

local = "C:/Users/gabgu/Desktop/MessyFolder"


def createFolders():

    global files
    files = os.listdir("C:/Users/gabgu/Desktop/MessyFolder")
    global typesFiles 
    typesFiles = []
    
    for i in range(0, len(files)):
        x = files[i].split(".")

        if not x[-1].upper() in typesFiles:
            typesFiles.append(x[-1].upper())
        

    for i in range(0, len(typesFiles) ):
        
        if  not typesFiles[i].upper() in files: 
            # print(typesFiles[i].upper())
            os.mkdir(str(local+"/"+typesFiles[i].upper()))
    
    moveFiles()
    
    

def moveFiles():
    files = os.listdir("C:/Users/gabgu/Desktop/MessyFolder")
    
    for i in range(0, len(files)):
        typefile = ""
        folder = ""
        if not files[i] in typesFiles:
            typefile = files[i].split(".")
            folder = typefile[-1].upper()

            sh.move(local+"/"+files[i], local+"/"+folder)
            
            



createFolders()


