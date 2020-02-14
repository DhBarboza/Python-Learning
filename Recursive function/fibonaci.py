#Calcule Fibonaci de um inteirto n
from functools import lru_cache
@ru_cache(maxsize=None)
def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)


