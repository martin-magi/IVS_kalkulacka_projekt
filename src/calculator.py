"""
@project IVS Kalkulačka
@file calculator.py
@brief Matematicka knižnica a logika kalkulačky
@author xlieskt00, Tamara Lieskovská
"""

import math

__all__ = [
    
    "add",
    "subtract",
    "multiply",
    "divide",
    "factorial",
    "power",
    "root",
    "modulo"
]

# =====================
# Zakladné operácie
# =====================

"""
    @func
    @brief 
    @param
    @param
    @return
"""
def add(a, b):
    return a + b

"""
    @func
    @brief 
    @param
    @param
    @return
"""
def subtract(a, b):
    return a - b

"""
    @func
    @brief 
    @param
    @param
    @return
"""
def multiply(a, b):
    return a * b

"""
    @func
    @brief 
    @param
    @param
    @exception
    @return
"""
def divide(a, b):
    if b == 0:
        raise ValueError("Math Error: Division by zero")
    return a / b

# =====================
# Pokročilé operácie
# =====================

"""
    @func
    @brief 
    @param
    @param
    @exception
    @return
"""
def factorial(n):
    if int(n) != n or n < 0:
        raise ValueError("Math Error:Factorial is only defined for non-negative integers")
    res = 1
    while n:
        res *= n
        n -= 1    
    return res
    
"""
    @func
    @brief 
    @param
    @param
    @exception
    @return
"""    
def power(base, exponent):
    if base == exponent and exponent < 0:
        raise ValueError("Math Error: Base is zero with negative exponent")
    return base ** exponent
    
"""
    @func
    @brief 
    @param
    @param
    @exception
    @return
"""    
def root(value, degree):
    if degree == 0:
        raise ValueError("Math Error: Cannot calculate root with degree 0")
    if value < 0:
        if degree % 2 == 0:
            raise ValueError("Math Error: Even root of negative number is not defined")
        return -((abs(value)) ** (1 / degree))
    return value ** (1 / degree)

"""
    @func
    @brief 
    @param
    @param
    @return
"""
def sin(degrees, terms=10):
    
    pi = 3.141592653589793

    # Convert degrees to radians
    x = degrees * (pi / 180)

    # Reduce x to range [−π, π] for better accuracy
    while x > pi:
        x -= 2 * pi
    while x < -pi:
        x += 2 * pi

    sine_approx = 0
    for n in range(terms):
        sign = (-1) ** n
        term = (x ** (2 * n + 1)) / factorial(2 * n + 1)
        sine_approx += sign * term
    return sine_approx

"""
    @func
    @brief 
    @param
    @param
    @exception
    @return
"""
def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    if a < 0:
        return -((abs(a) % b))
    return a % b

"""
    @func
    @brief 
    @param
    @param
    @exception
    @return for now always returns 0
"""
def eval(expr):
    return 0
