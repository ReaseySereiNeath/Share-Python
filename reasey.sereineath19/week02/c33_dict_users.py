def dict_users(list1):
    dictList = []
    for i in range(len(list1)):
        theDict = {"username:": list1[i], "ID": i+1}
        dictList.append(theDict)
    return dictList
