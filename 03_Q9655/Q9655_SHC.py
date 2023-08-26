"""
돌 게임
"""


def sol(n: int) -> bool:
    memo = [0 for _ in range(max(4, n + 2))]
    memo[1] = 0
    memo[2] = 1
    memo[3] = 0

    for i in range(4, n + 1):
        memo[i] = min(memo[i - 1] ^ 1, memo[i - 3] ^ 1)

    return bool(memo[n])


if __name__ == "__main__":
    print("CY" if sol(int(input())) else "SK")
