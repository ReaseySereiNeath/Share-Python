def dict_shopping(dictionary1):
    res = 0
    qua = 0
    if len(dictionary1) < 1:
        return("Invalid JSON", 0)
    for i in dictionary1:
        if "price" in i and "quantity" in i:
            if len(i) != 2 or i["price"] < 0.01 or i["quantity"] < 1:
                return ("Invalid JSON", 0)
            else:
                a = i["price"]*i["quantity"]
                b = i["quantity"]
                res = res+a
                qua = qua+b
        else:
            return ("Invalid JSON", 0)
    res = round(res,2)
    return("$"+str(res), qua)    

