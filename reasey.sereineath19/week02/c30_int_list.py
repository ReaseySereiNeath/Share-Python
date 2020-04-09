def int_list(list1):
#if len(list1) = 0:
#   return False;

    for i in range(len(list1)):
        if all(isinstance(list1[i], int) for i in list1):
            return True
        else:
            return False
    return False

print(int_list([1,2,3,4,5]))