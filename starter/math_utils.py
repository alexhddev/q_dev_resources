from typing import List, Union

Number = Union[int, float]

def sum(a: Number, b: Number) -> Number:
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a+b

def sum_array(arr: List[Number]) -> Number:
    """Calculate sum of all numbers in array.
    
    Args:
        arr: List of numbers
        
    Returns:
        Sum of all numbers in the array
    """
    sum = 0
    for i in arr:
        sum += i
    return sum

def average(arr: List[Number]) -> float:
    """Calculate average of numbers in array.
    
    Args:
        arr: List of numbers
        
    Returns:
        Average of all numbers in the array
    """
    return sum_array(arr)/len(arr)

def sub(a: Number, b: Number) -> Number:
    """Subtract two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of a and b (a - b)
    """
    return a-b

def mul(a: Number, b: Number) -> Number:
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a*b

def div(a: Number, b: Number) -> float:
    """Divide two numbers.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Quotient of a divided by b
    """
    return a/b

def mod(a: Number, b: Number) -> Number:
    """Calculate modulo of two numbers.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Remainder of a divided by b
    """
    return a%b

def pow(a: Number, b: Number) -> Number:
    """Raise number to a power.
    
    Args:
        a: Base number
        b: Exponent
        
    Returns:
        a raised to the power of b
    """
    return a**b