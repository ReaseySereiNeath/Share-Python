def odd_even_list(list):
    oddEven_list = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            oddEven_list.append("EVEN")
        else:
            oddEven_list.append('ODD')
    return oddEven_list
        
    


