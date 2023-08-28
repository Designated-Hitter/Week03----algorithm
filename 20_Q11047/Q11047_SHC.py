"""
동전 0
"""

from bisect import bisect_right
from sys import stdin

input = stdin.readline

standard_input = """10 4200
1
5
10
50
100
500
1000
5000
10000
50000
"""


n, k = (int(x) for x in input().split())

A = [int(input().strip()) for _ in range(n)]  # already sorted

cnt = 0

while k > 0:
    idx = bisect_right(A, k)
    mult = k // A[idx - 1]
    cnt += mult
    k -= A[idx - 1] * mult

print(cnt)
