import random
def gen_passwords(chars, length, numbers):
    list1 = []
    for p in range(numbers):
        password = ''
        for i in range(length):
            password = password + random.choice(chars)
        list1.append(password)
    return list1