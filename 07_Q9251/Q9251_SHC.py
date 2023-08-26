"""
LCS
"""

from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10**8)


@lru_cache(256)
def LCS(X: str, Y: str) -> int:
    """X와 Y의 최장 공통부분수열의 길이를 구한다."""
    if len(X) == 0 or len(Y) == 0:
        return 0

    if X[-1] == Y[-1]:
        # 두 접두어가 같은 문자로 끝난다 => LCS의 멤버임이 확실
        return LCS(X[:-1], Y[:-1]) + 1
    # 두 접두어가 다른 문자로 끝난다. xn을 살리는 쪽과 yn을 살리는 쪽
    # 둘 중에 더 긴 녀석을 선택한다.
    return max(LCS(X[:-1], Y), LCS(X, Y[:-1]))


if __name__ == "__main__":
    X = input()
    Y = input()
    print(LCS(X, Y))
