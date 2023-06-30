import os 


def createFolder():
    os.mkdir("C:/Users/gabgu/Desktop/MessyFolder")
    print("Folder to created !")


def deleteFolder():
    answer = str(input("You want delete this folder ?"))

    if answer == "no":
        return
    if answer == "yes":
        os.rmdir("C:/Users/gabgu/Desktop/MessyFolder")
        print("Folder to deleted !")
    else:
        deleteFolder()

createFolder()
deleteFolder()