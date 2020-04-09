ch1 = input("Enter something: ")
ch1.find("#")
if "#" in ch1:
    x = ch1.index("#")
    print(ch1[:x])
else:
    print(ch1)


