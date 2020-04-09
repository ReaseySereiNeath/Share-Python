import re
def regex_para(string):
    if len(string) <= 0:
        return '""'
    else:
        return re.sub(r" ?\([^)]+\)", "",string)

#print(regex_para("(hello) Welcome to KIT (Kirirom Institue of Technology)!"))
