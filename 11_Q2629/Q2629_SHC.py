"""
양팔저울
"""

from sys import stdin

MAX_WEIGHT = 40
MAX_N = 7


def r_sol(idx: int, weight: int):
    if g_visited[idx][weight]:
        return

    g_visited[idx][weight] = True

    if idx >= len(W):
        return

    r_sol(idx + 1, weight + W[idx])
    r_sol(idx + 1, weight)  # pass
    r_sol(idx + 1, abs(weight - W[idx]))


# key: weight, value: quantity
W: list[int]
# visited[idx][weight]: idx번째 추 까지 사용하여 weight를 만들 수 있는가?
g_visited: list[list[bool]]


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    W = sorted(int(x) for x in stdin.readline().split())

    k = int(stdin.readline().strip())
    marbles = [int(x) for x in stdin.readline().split()]

    g_visited = [[False for _ in range(MAX_WEIGHT + 1)] for _ in range(n + 1)]

    r_sol(0, 0)

    for marble in marbles:
        if marble > MAX_WEIGHT:
            print("N", end=" ")
        elif g_visited[n][marble]:
            print("Y", end=" ")
        else:
            print("N", end=" ")
    print()
