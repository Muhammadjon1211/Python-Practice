def math_oprt(a,b):
    return a+b, a-b, a*b, a/b, a**b, a//b, a%b

def math_oprt1(a,b):
    a+=b
    return a
print(math_oprt1(5,2))

def math_oprt2(a,b):
    a-=b
    return a
print(math_oprt2(5,2))

def math_oprt3(a,b):
    a/=b
    return a
print(math_oprt3(5,2))

def math_oprt4(a,b):
    a*=b
    return a
print(math_oprt4(5,2))


qoldiq = 7.68
butun = int(qoldiq)
print(qoldiq, butun)

def math_square_add(a,b):
    return a**2 + b**2
print(math_square_add(2,3))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def ecube(a,b):
    if a**3>b**3:
        return a**3
    else:
        return b**3
print(ecube(2,3))

import math
def math_square(a):
    return math.sqrt(a)
print(math_square(4))

def math_pi(n):
    return math.pi * n**2
print(math_pi(5))

def math_factorial(n):
    return math.factorial(n)
print(math_factorial(5))

def math_log(a):
    return math.log(a)
print(math_log(5))

def math_cos(a):
    return math.cos(a)
print(math_cos(5))

