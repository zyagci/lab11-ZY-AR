# https://github.com/zyagci/lab11-ZY-AR
# Partner 1: Zeynep Yagci
# Partner 2: Afifa Rahman

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):   # raise ZeroDivisionError if a == 0
    if b == 0:
        raise ZeroDivisionError("Cannot Divide by Zero.")
    return b/a


def logarithm(a, b): # use math library/raise ValueError
    if a <= 0 or a == 1:
        raise ValueError("Base must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Argument must be grater than 0.")
    return math.log(b, a)


def exponent(a, b):
    return a ** b



