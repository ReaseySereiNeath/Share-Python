def list_number(start, end, reversed=False):
    list1 = []
    if reversed == True:
        for i in range(end, start-1, -1):
            list1.append(i)
        return list1
    else:
        for i in range(start, end+1, 1):
            list1.append(i)
        return list1


