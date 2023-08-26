"""
동전 2
"""

from sys import maxsize, stdin


INF = maxsize

n, k = [int(x) for x in stdin.readline().split()]  # n: 종류, k: 목표금액
coins = [int(stdin.readline().strip()) for _ in range(n)]
dp = [INF for _ in range(k + 1)]

dp[0] = 0

for i in range(1, k + 1):
    for coin in coins:
        if coin > i:
            continue
        dp[i] = min(dp[i], dp[i - coin] + 1)  # 조합이 아니라 동전의 **숫자**임

print(dp[k] if dp[k] != INF else -1)
