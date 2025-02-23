def add(a, b):
    return a + b

def subtract(a, b):
    return abs(a - b)

def divide(a, b):
    if a == 0 or b == 0:
        raise ValueError("Division by zero is not allowed.")
    
    larger = max(a, b)
    smaller = min(a, b)
    return larger // smaller

def multiply(a, b):
    return a * b
def Test(Pred, Ref):
    return Pred==Ref
from arithmetics import add, subtract, divide, multiply

def sumlist(arr):
    result = 0
    for num in arr:
        result = add(result, num)
    return result

def mullist(arr):
    result = 1
    for num in arr:
        result = multiply(result, num)
    return result

def remlist(arr1, arr2):
from arithmetics import divide, multiply, subtract

def remList(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Both lists must have the same length.")
    
    result = []
    for a, b in zip(arr1, arr2):
        larger = max(a, b)
        smaller = min(a, b)
        if smaller == 0:
            raise ValueError("Division by zero is not allowed.")
        quotient = divide(larger, smaller) 
        product = multiply(smaller, quotient)
        remainder = subtract(larger, product)
        result.append(remainder)
    
    return result
print("Arithmetics module is imported")