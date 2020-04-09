from itertools import product

def all_passwords(characters, length):
    list1 = []
    for i in product(characters, repeat=length):
        list1.append(''.join(i))
    list1 = sorted(set(list1))
    return list1
