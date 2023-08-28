"""
LCS 2
"""

from enum import Enum, auto
from typing import Callable


class Dir(Enum):
    SE = auto()
    E = auto()
    S = auto()


def LCS(X: str, Y: str, hook: Callable[[int, int, Dir], None]) -> int:
    """X와 Y의 최장 공통부분수열의 길이를 구한다."""
    # ∵ 빈 수열도 비교해야 하기 때문. (초기조건)
    dp = [[0 for _ in range(len(Y))] for _ in range(len(X))]
    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if X[i] == Y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                hook(i, j, Dir.SE)
            elif dp[i - 1][j] > dp[i][j - 1]:
                hook(i, j, Dir.S)
                dp[i][j] = dp[i - 1][j]
            else:
                hook(i, j, Dir.E)
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]


class Tracer:
    """공통부분수열의 문자열을 찾기 위해 만든 클래스"""

    dp: list[list[Dir]]

    def __init__(self, xlen: int, ylen: int):
        self.dp = [[Dir.E for _ in range(ylen)] for _ in range(xlen)]

    def hook(self, i: int, j: int, d: Dir):
        self.dp[i][j] = d


if __name__ == "__main__":
    X = input()
    Y = input()
    X = " " + X
    Y = " " + Y
    tracer = Tracer(len(X), len(Y))
    lcs_len = LCS(X, Y, tracer.hook)
    print(lcs_len)

    if lcs_len > 0:
        # tracer 안에 있는 정보를 역으로 추적해가며 문자열을 생성한다.
        result = ""
        x = len(X) - 1
        y = len(Y) - 1
        while x > 0 and y > 0:
            match tracer.dp[x][y]:
                case Dir.E:
                    y -= 1
                case Dir.S:
                    x -= 1
                case Dir.SE:
                    result += X[x]
                    x -= 1
                    y -= 1
        print(result[::-1])
