def dict_search(info_students, var1):
    for i in info_students:
        if var1 in info_students:
            return info_students[var1]
        else:
            return ("ERROR: '"+var1+"' key not found.")

