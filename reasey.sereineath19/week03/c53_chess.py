def gen_chessboard(height=8, width=8):
    if height < 2 or width < 2 or height % 2 != 0 or width % 2 != 0:
        return None
    list1 = []
    for i in range(height):
        if i % 2 != 0:
            list1.append([0, 1]*int(width/2))
        else:
            list1.append([1, 0]*int(width/2))
    return list1


print(gen_chessboard())
