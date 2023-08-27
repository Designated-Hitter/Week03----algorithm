"""
문자열 판별

메모리:
실행시간:
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
    start = 0
    end = 1
    A_HASH = {djbc2(a) for a in A}

    while end <= len(S):
        sample = S[start:end]
        if djbc2(sample) in A_HASH:
            start = end
        end += 1
    return start == end - 1


if __name__ == "__main__":
    S = stdin.readline().strip()
    n = int(stdin.readline().strip())
    A = [stdin.readline().strip() for _ in range(n)]

    print(1 if sol(S, A) else 0)
