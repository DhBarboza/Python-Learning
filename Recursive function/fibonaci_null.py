f = {}
def fib(n):
    if n <= 2: return 1
    if n not in f: f[n] = fib(n-1) + fib(n-2)
    return f[n]
