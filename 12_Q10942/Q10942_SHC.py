"""
팰린드롬?
"""


from functools import cache
from sys import setrecursionlimit, stdin

setrecursionlimit(10**8)


@cache
def r_sol(i: int, j: int) -> bool:
    if i == j:
        return True
    return N[i] == N[j] and r_sol(i + 1, j - 1)


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    N = [int(x) for x in stdin.readline().split()]
    m = int(stdin.readline().strip())

    for s, e in ((int(x) - 1 for x in stdin.readline().split()) for _ in range(m)):
        print(1 if r_sol(s, e) else 0)
