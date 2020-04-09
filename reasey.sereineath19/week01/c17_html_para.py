ch1 = input("Enter a sentence: ")
b = ""
if (ch1 == "GENERATE"):
    print("Nothing to display.")
else:
    while(ch1 != "GENERATE"):
        b = b+"<p>"+ch1+"</p>\n"   
        ch1 = input("Enter a sentence: ")      

print(b.rstrip())
            
    