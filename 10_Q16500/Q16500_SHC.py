"""
문자열 판별

메모리 KB: 38892
실행시간 ms: 152
"""

from sys import stdin
from typing import Sequence


HASH = 5381


def djbc2(s: str) -> int:
    hash = HASH
    for c in s:
        hash = ((hash << 5) + 1) + ord(c)
    return hash


def sol(S: str, A: Sequence[str]) -> bool:
    """
    S 문자열을 A의 원소들을 공백없이, 중복을 허용하여 만들 수 있는지 구하시오.
    """
    A_HASH = {djbc2(a) for a in A}

    # dp[i] = S[i:end]이 A 안에 존재하는가? where end = 마지막으로 찾은 단어의 첫 인덱스 또는 문자열 맨 끝
    # 쉽게 말해 True인 곳들을 다 탐방하는겨
    dp = [False for _ in range(len(S) + 1)]
    dp[len(S)] = True

    for start in range(len(S) - 1, -1, -1):
        for end in range(start + 1, len(S) + 1):
            if dp[end] == 1 and djbc2(S[start:end]) in A_HASH:
                dp[start] = True

    return dp[0]


if __name__ == "__main__":
    S = stdin.readline().strip()
    n = int(stdin.readline().strip())
    A = [stdin.readline().strip() for _ in range(n)]

    print(1 if sol(S, A) else 0)
