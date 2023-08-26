"""
동전
"""

from functools import cache


def sol(cost: int, coins: list[int]) -> int:
    ...


g_coins = []


@cache
def r_sol(n: int, k: int) -> int:
    """
    dp[n][k]: n원을 만들기 위해 0~k번째 동전을 사용하는 경우의 수
    """
    if k == 0:
        return 1

    result = 0
    for coin in g_coins:
        result += r_sol(n - coin, k - 1)
    return result
