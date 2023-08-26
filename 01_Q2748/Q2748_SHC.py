"""
피보나치 수 2
"""

from functools import cache


@cache
def r_fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return r_fib(n - 1) + r_fib(n - 2)


print(r_fib(int(input())))
