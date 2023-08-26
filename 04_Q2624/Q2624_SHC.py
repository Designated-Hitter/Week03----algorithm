"""
동전 바꿔주기
"""

from sys import stdin


Val = int  # valuable
Amt = int  # amount


def sol(t: int, coins: list[tuple[Val, Amt]]) -> int:
    """
    `dp[n][k]` = n원을 1~k번째 동전으로 만드는 경우의 수

    ```python
       dp[n][k] = sum( dp[n - (value * cnt)][k - 1] for value, cnt in coins )
    ```
    where coins = `list[tuple[Val, Amt]]`

    """
    coins.sort(key=lambda tup: tup[0])
    # row = 목표금액 'n'
    # col = 사용할 동전의 종류, 1번부터 'k' 까지
    dp = [[0 for _ in range(len(coins))] for _ in range(t + 1)]

    # dp[n][0] 부터 채우자
    for n in range(t + 1):
        dp[n][0] = 1 if n <= coins[0][1] else 0

    # 그리고 row를 우선적으로 채워나가면서 문제를 풀어보자.
    for k in range(1, len(coins)):
        coin_value = coins[k][0]
        coin_amount = coins[k][1]
        for n in range(t + 1):
            for amt in range(coin_amount + 1):
                total_value = coin_value * amt
                if total_value <= n:
                    dp[n][k] += dp[n - total_value][k - 1]

    return dp[t][len(coins) - 1]


if __name__ == "__main__":
    t = int(stdin.readline().strip())
    k = int(stdin.readline().strip())
    coins = [tuple(int(x) for x in stdin.readline().split()) for _ in range(k)]

    print(sol(t, coins))
