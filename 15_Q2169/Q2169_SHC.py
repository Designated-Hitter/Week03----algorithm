"""
로본 조종하기
ref: https://child-developer.tistory.com/87
"""

from sys import stdin


input = stdin.readline

n, m = (int(x) for x in input().split())

# init dp
dp = [[int(x) for x in input().split()] for _ in range(n)]

for j in range(1, m):
    dp[0][j] += dp[0][j - 1]

for i in range(1, n):
    l2r = dp[i][:]
    r2l = dp[i][:]

    # left to right
    for j in range(m):
        if j == 0:
            # only chance for downward
            l2r[j] += dp[i - 1][j]
        else:
            l2r[j] += max(dp[i - 1][j], l2r[j - 1])
    # right to left
    for j in range(m - 1, -1, -1):
        if j == m - 1:
            # only chance for downward
            r2l[j] += dp[i - 1][j]
        else:
            r2l[j] += max(dp[i - 1][j], r2l[j + 1])

    for j in range(m):
        dp[i][j] = max(l2r[j], r2l[j])

print(dp[n - 1][m - 1])
