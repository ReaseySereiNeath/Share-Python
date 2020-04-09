def dict_count(list1):
    count = {} 

    for i in list1:
        count[str(i)] = list1.count(i)
    return count