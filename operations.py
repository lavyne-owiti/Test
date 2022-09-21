def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError('can not divide by zero!')
    return x/y

print(add(10,5))