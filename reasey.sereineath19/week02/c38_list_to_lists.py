def list_to_lists(list1):
    list2 = []
    for i in list1:
        list3 = []
        for j in i:
            list3.append(j)
        list4=list3[::-1]
        list2.append(list4)
    return list2