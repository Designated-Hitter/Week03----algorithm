"""
양팔저울
메모리      시간
34440     60
"""

from sys import stdin

MAX_WEIGHT = 30 * 500
MAX_N = 7


def r_sol(N: int, idx: int, weight: int):
    """
    0번째부터 idx번째 추 까지 사용하여 weight를 만들 수 있는가?
    """
    if g_visited[idx][weight]:
        return

    g_visited[idx][weight] = True

    if not (0 <= idx < N):
        return

    r_sol(N, idx + 1, weight + W[idx + 1])  # 추에 무게를 더하는 경우
    r_sol(N, idx + 1, weight)  # pass
    r_sol(N, idx + 1, abs(weight - W[idx + 1]))  # 반대쪽에 추를 다는 경우


# key: weight, value: quantity
W: list[int]
# visited[idx][weight]: idx번째 추 까지 사용하여 weight를 만들 수 있는가?
g_visited: list[list[bool]]


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    W = [int(x) for x in stdin.readline().split()] + [0]  # dummy index for index safety

    k = int(stdin.readline().strip())
    marbles = [int(x) for x in stdin.readline().split()]

    g_visited = [[False for _ in range(MAX_WEIGHT + 1)] for _ in range(n + 1)]

    # init visited
    r_sol(n, 0, W[0])
    r_sol(n, 0, 0)

    for marble in marbles:
        if marble > MAX_WEIGHT:
            # 추가 만들어낼 수 있는 최대 무게는 30 * 500인데 입력으로 들어올 수 있는 구슬의 무게는 최대 40_000이라서
            print("N", end=" ")
        elif g_visited[n][marble]:
            print("Y", end=" ")
        else:
            print("N", end=" ")
    print()
