def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def mod(a,b):
    return a%b
def pow(a,b):
    return a**b
def floor_div(a,b):
    return a//b

def sqrt(a):
    return a**0.5

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a