"""
팰린드롬?
"""
from sys import setrecursionlimit, stdin

MAXN = 2000
setrecursionlimit(10**8)
g_dp = [[False for _ in range(MAXN + 1)] for _ in range(MAXN + 1)]


def r_sol(i: int, j: int) -> bool:
    if i == j:
        return True
    if g_dp[i][j]:
        return g_dp[i][j]

    if N[i] == N[j]:
        result = r_sol(i + 1, j - 1)
        g_dp[i][j] = result

    return g_dp[i][j]


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    N = [int(x) for x in stdin.readline().split()]
    m = int(stdin.readline().strip())

    for i in range(MAXN + 1):
        g_dp[i][i] = True

    r_sol(0, m)

    for s, e in ([int(x) - 1 for x in stdin.readline().split()] for _ in range(m)):
        print(1 if g_dp[s][e] else 0)
