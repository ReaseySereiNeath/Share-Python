def fun_add(a,b):
    sum = a + b
    return sum
def fun_sub(a,b):
    sub = a - b
    return sub
def fun_mul(a,b):
    mul = a * b
    return mul
def fun_div(a,b):
    div = a / b
    if a % b == 0:
        return int(div)
    else:
        return float(div)


