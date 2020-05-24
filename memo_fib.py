def fib(n):
    if(n <= 2): return n
    return (fib(n-2) + fib(n-1))

cache = {}
def fibb(n):
    if n in cache: return cache[n]

    if n<=2: value = n

    if n>2: value = fibb(n-1) + fibb(n-2)

    cache[n] = value
    return value

from functools import lru_cache
@lru_cache
def fib(n):
    if(n<0 or type(n) != int): 
        raise ValueError("input must be a positive int")
    if(n <= 2): return n
    return (fib(n-2) + fib(n-1))

print(fib(30))
