"""
컵라면
"""

from dataclasses import dataclass
from functools import total_ordering
from heapq import heappop, heappush
from sys import stdin
from typing import Self


@dataclass
@total_ordering
class Ramyeon:
    deadline: int
    ramyeon: int

    def __lt__(self, o: Self) -> bool:
        if self.deadline == o.deadline:
            return self.ramyeon > o.ramyeon
        return self.deadline < o.deadline

    def __eq__(self, o: Self) -> bool:
        return self.deadline == o.deadline and self.ramyeon == o.ramyeon

    def __gt__(self, o: Self) -> bool:
        return o < self


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    ramyeons = sorted(Ramyeon(*(int(x) for x in stdin.readline().split())) for _ in range(n))
    minheap = []
    for r in ramyeons:
        heappush(minheap, r.ramyeon)
        if len(minheap) > r.deadline:
            heappop(minheap)
    print(sum(minheap))
