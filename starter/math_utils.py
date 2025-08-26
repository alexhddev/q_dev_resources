
def sum(a,b):
    return a+b

def sum_array(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def average(arr):
    return sum_array(arr)/len(arr)

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def mod(a, b):
    return a%b

def pow(a, b):
    return a**b