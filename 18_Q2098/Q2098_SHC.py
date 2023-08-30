"""
외판원 순회
"""

from sys import stdin
from lib.bitset import Bitset


input = lambda: stdin.readline().strip()
INF = (1 << 31) - 1

N = int(input())
G = [[INF if x == "0" else int(x) for x in input().split()] for _ in range(N)]

bitset = Bitset(N)


def dfs(x, visited):
    ...
