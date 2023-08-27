"""
양팔저울
"""

from collections import defaultdict
from functools import cache
from sys import stdin


@cache
def r_sol(weight: int, visited: list[int]) -> bool:
    """weight 무게를 추들의 모임 W를 사용해서 만들 수 있는가?"""
    global W
    if 


# key: weight, value: quantity
W: dict[int, int] = defaultdict(int)


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    for weight in (int(x) for x in stdin.readline().split()):
        W[weight] += 1

    print(W)

    k = int(stdin.readline().strip())
    marbles = [int(x) for x in stdin.readline().split()]

    print(" ".join("Y" if r_sol(marble) else "N" for marble in marbles))
