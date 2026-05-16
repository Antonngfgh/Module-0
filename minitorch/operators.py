"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a: float, b: float) -> float:
    return a * b

def id(x: float) -> float:
    return x

def add(a: float, b: float) -> float:
    return a + b

def neg(x: float) -> float:
    return -x

def lt(a: float, b: float) -> bool:
    return a < b

def eq(a: float, b: float) -> bool:
    return is_close(a, b)

def max(a: float, b: float) -> float:
    return a if a > b else b

def is_close(a: float, b: float) -> bool:
    return abs(a - b) < 1e-2

def sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + exp(-x))
    else:
        return exp(x) / (1.0 + exp(x))

def relu(x: float) -> float:
    return max(0, x)

def log(x: float) -> float:
    return math.log(x)

def exp(x: float) -> float:
    return math.exp(x)

def log_back(a: float, b: float) -> float:
    return b / a

def inv(x: float) -> float:
    return 1.0 / x

def inv_back(a: float, b: float) -> float:
    return -b / (a * a)

def relu_back(x: float, grad: float) -> float:
    return grad if x > 0 else 0.0
# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(fn: Callable[[float], float], 
    lst: Iterable[float]
) -> list:
    return [fn(x) for x in lst]

def zipWith(
    fn: Callable[[float, float], float],
    lst1: Iterable[float],
    lst2: Iterable[float]
) -> list:
    min_len = min(len(lst1), len(lst2))
    return [fn(lst1[i], lst2[i]) for i in range(min_len)]

def reduce(fn: Callable[[float, float], float], lst: Iterable[float], initial: float) -> float:
    r = initial
    for x in lst:
       r = fn(r, x)
    return r


def negList(lst: Iterable[float]) -> list:
    return map(neg, lst)

def addLists(lst1: Iterable[float], lst2: Iterable[float]) -> list:
    return zipWith(add, lst1, lst2)

def sum(lst: Iterable[float]) -> float:
    return reduce(add, lst, 0.0)

def prod(lst: Iterable[float]) -> float:
    return reduce(mul, lst, 1.0)