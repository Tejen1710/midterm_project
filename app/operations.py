
import math
from typing import Callable, Dict
from .exceptions import OperationError

def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b

def divide(a,b):
    if b == 0: raise OperationError("Division by zero")
    return a/b

def power(a,b): return a**b

def root(a,b):
    if b == 0: raise OperationError("0th root undefined")
    # For even roots of negative values, disallow
    if a < 0 and int(b) % 2 == 0:
        raise OperationError("Even root of a negative number is not real")
    # handle general nth root
    return math.copysign(abs(a)**(1.0/float(b)), 1)

def modulus(a,b):
    if b == 0: raise OperationError("Modulus by zero")
    return a % b

def int_divide(a,b):
    if b == 0: raise OperationError("Integer division by zero")
    return math.trunc(a / b)

def percent(a,b):
    if b == 0: raise OperationError("Percent with zero denominator")
    return (a / b) * 100.0

def abs_diff(a,b): return abs(a-b)

_OPS: Dict[str, Callable[[float,float], float]] = {
    "add": add, "subtract": subtract, "multiply": multiply, "divide": divide,
    "power": power, "root": root, "modulus": modulus, "int_divide": int_divide,
    "percent": percent, "abs_diff": abs_diff,
    "+": add, "-": subtract, "*": multiply, "/": divide, "^": power
}

def get_operation(name: str) -> Callable:
    try:
        return _OPS[name]
    except KeyError as e:
        raise OperationError(f"Unknown operation: {name}") from e
