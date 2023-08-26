"""
01타일
"""

MOD = 15746


def sol(n: int):
    memo = [1 for _ in range(n + 1)]  # [0] unused
    memo[2] = 2
    for i in range(3, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % MOD
    return memo[n]


if __name__ == "__main__":
    print(sol(int(input())))
