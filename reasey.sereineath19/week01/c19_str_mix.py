ch1 = input("Enter a word: ")
if len(ch1) == 2:
    print(ch1*2)
elif len(ch1) == 1:
    print(ch1*4)
elif len(ch1) == 0:
    print(ch1*4)
else:
    rev1 = (ch1[1::-1])
    rev2 = (ch1[-1:-3:-1])
    new_rev = rev1 + rev2
    print(new_rev)