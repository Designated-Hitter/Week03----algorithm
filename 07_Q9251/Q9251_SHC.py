"""
LCS
"""


def LCS(X: str, Y: str) -> int:
    """X와 Y의 최장 공통부분수열의 길이를 구한다."""
    # ∵ 빈 수열도 비교해야 하기 때문. (초기조건)
    X = " " + X
    Y = " " + Y
    dp = [[0 for _ in range(len(Y))] for _ in range(len(X))]
    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if X[i] == Y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


if __name__ == "__main__":
    X = input()
    Y = input()
    print(LCS(X, Y))
