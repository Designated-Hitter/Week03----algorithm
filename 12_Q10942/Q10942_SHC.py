"""
팰린드롬?
"""
from sys import stdin

MAXN = 2000


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    N = [int(x) for x in stdin.readline().split()]
    m = int(stdin.readline().strip())
    g_dp = [[False for _ in range(n)] for _ in range(n)]

    # 길이 1짜리 문자열은 언제나 펠린드롬
    for i in range(n):
        g_dp[i][i] = True

    # 길이 2짜리 문자열은 두 문자가 같아야만 펠린드롬
    for i in range(n - 1):
        if N[i] == N[i + 1]:
            g_dp[i][i + 1] = True

    # 길이 3 이상부터는 재귀적 관계로 이어간다.
    for cnt in range(2, n):
        for s in range(n - cnt):
            e = s + cnt
            if N[s] == N[e] and g_dp[s + 1][e - 1]:
                g_dp[s][e] = True

    for s, e in ((int(x) - 1 for x in stdin.readline().split()) for _ in range(m)):
        print(1 if g_dp[s][e] else 0)
