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

    COL = len(coins)  # coin의 종류
    ROW = t + 1  # 금액

    dp = [[0 for _ in range(COL)] for _ in range(ROW)]

    # 0's COL을 먼저 채우자
    coin0 = coins[0]
    cnt = 0
    for r in range(ROW):
        if cnt <= coin0[1] and r % coin0[0] == 0:
            # 개수가 모자라도 안되고 r의 약수가 아니어도 안된다.
            cnt += 1
            dp[r][0] = 1
        else:
            dp[r][0] = 0
    del cnt

    # 1's COL부터 차근차근
    for c in range(1, COL):
        coin_val = coins[c][0]
        coin_amt = coins[c][1]

        for r in range(ROW):
            for cnt in range(min(r // coin_val, coin_amt) + 1):
                coin_acc = coin_val * cnt  # 0 inclusive
                dp[r][c] += dp[r - coin_acc][c - 1]
    return dp[ROW - 1][COL - 1]


if __name__ == "__main__":
    t = int(stdin.readline().strip())
    k = int(stdin.readline().strip())
    coins = [tuple(int(x) for x in stdin.readline().split()) for _ in range(k)]

    print(sol(t, coins))
