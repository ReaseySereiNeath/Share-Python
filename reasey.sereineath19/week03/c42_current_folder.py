import os


def current_folder():
    list1 = []
    fileNames = os.listdir(".")
    for i in fileNames:
        if os.path.isfile(i):
            theDict = {"filename": i, "type": 'File'}
            list1.append(theDict)
        else:
            theDict = {"filename": i, "type": 'Folder'}
            list1.append(theDict)
    return list1
