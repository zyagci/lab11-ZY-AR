# https://github.com/zyagci/lab11-ZY-AR
# Partner 1: Zeynep Yagci
# Partner 2: Afifa Rahman

"""
calculator.py
Defines functions used to create a simple calculator.
"""

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Argument must be greater than 0.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)


