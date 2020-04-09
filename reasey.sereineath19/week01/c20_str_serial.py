ch1 = input("Enter: ")
x = ch1.replace(" ", "")
if len(x) == 0:
    print("EMPTY")
else:
    n = 1
    for i in x:
        if n <len(x):
            b = i * n
            print(b.capitalize(), end="-")
            n=n+1
        elif n == len(x):
            b = i*n
            print(b.title())
