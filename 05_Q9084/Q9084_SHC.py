"""
동전
"""

from sys import stdin

if __name__ == "__main__":
    t = int(stdin.readline().strip())

    for _ in range(t):
        n = int(stdin.readline().strip())
        g_coins = sorted(int(x) for x in stdin.readline().split())
        m = int(stdin.readline().strip())

        dp = [0 for _ in range(m + 1)]
        dp[0] = 1
        for i in range(n):
            # 동전 i까지의 dp에 대하여
            for j in range(g_coins[i], m + 1):
                # j만큼의 금액에 대하여
                dp[j] += dp[j - g_coins[i]]

        print(dp[m])
