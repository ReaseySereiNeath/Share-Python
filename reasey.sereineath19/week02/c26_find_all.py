def find_all(list, value):
    if value in list:
        indexList = []
        for i in range(len(list)):
            if list[i] == value:
                indexList.append(i)
        return indexList   
    else:
        return 'None'
def find_first(list, value):
    if value in list:
        return list.index(value)
    else:
        return 'None'