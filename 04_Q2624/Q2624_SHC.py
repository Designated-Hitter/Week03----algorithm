"""
동전 바꿔주기
"""

from sys import stdin


Val = int  # valuable
Amt = int  # amount


def sol(t: int, coins: list[tuple[Val, Amt]]) -> int:
    memo = [0 for _ in range(t + 1)]
    left = [amount for _, amount in coins]  # 몇개가 남았는지

    for i in range(1, t + 1):
        memo[i] = memo[i - 1]
        for coin, _ in coins:
            if i >= coin and left[coin] > 0:
                memo[i] += memo[i - coin] + 1
                left[coin] -= 1


if __name__ == "__main__":
    t = int(stdin.readline().strip())
    k = int(stdin.readline().strip())
    coins = [tuple(int(x) for x in stdin.readline().split()) for _ in range(k)]

    print(sol(t, coins))
