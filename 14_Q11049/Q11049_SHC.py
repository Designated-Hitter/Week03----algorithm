"""
행렬곱셈순서
ref: https://whatryando.tistory.com/97
"""

from sys import stdin

input = stdin.readline

N = int(input().strip())
INF = 1 << 31

arrs = [[int(x) for x in input().split()] for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(N - i):
        x = j + i
        dp[j][x] = INF
        for k in range(j, x):
            dp[j][x] = min(
                dp[j][x], dp[j][k] + dp[k + 1][x] + arrs[j][0] * arrs[k][1] * arrs[x][1]
            )
print(dp[0][N - 1])
