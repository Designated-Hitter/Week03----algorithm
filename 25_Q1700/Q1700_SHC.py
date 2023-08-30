"""
멀티탭 스케쥴링
"""

from dataclasses import dataclass
from functools import total_ordering
from heapq import heapify, heappop, heappush
from sys import stdin
from typing import Iterable, Self

INF = 1 << 31


@dataclass
@total_ordering
class Gadgetry:
    id: int  # 전자기기의 번호
    occurrence: int  # 전자기기가 몇 턴 후에 다시 등장하는지

    def __lt__(self, o: Self) -> bool:
        """maxheap"""
        return self.occurrence > o.occurrence

    def __eq__(self, o: Self) -> bool:
        return self.id == o.id

    def __gt__(self, o: Self) -> bool:
        return o < self

    def __repr__(self) -> str:
        return f"({self.id}, {self.occurrence})"


def sol(n: int, k: int, order: Iterable[int]) -> int:
    order = list(order)
    gadgetries: list[Gadgetry] = []

    for i in range(len(order)):
        j = i + 1
        while j < len(order):
            if order[i] == order[j]:
                break
            j += 1
        if j == len(order):
            j = INF
        gadgetries.append(Gadgetry(order[i], j - i))

    maxheap: list[Gadgetry] = []
    cnt = 0
    for gadget in gadgetries:
        is_updated = False
        for i in range(len(maxheap)):
            if maxheap[i] == gadget:
                maxheap[i] = gadget
                heapify(maxheap)
                is_updated = True
                break

        if is_updated:
            continue

        if len(maxheap) > n - 1:
            cnt += 1
            heappop(maxheap)
        heappush(maxheap, gadget)

    return cnt


def find_latest_used(plugs: set[int], order: list[int]) -> int:
    """
    - return: plugs 안에 있는 원소들 중 출현시기가 가장 늦는 (혹은 아예 없는) 원소번호를 리턴한다.
    """
    n = len(order)
    result = 0
    max_idx = -1

    for num in plugs:
        try:
            num_idx = order.index(num)
        except ValueError:
            num_idx = n
        if max_idx < num_idx:
            max_idx = num_idx
            result = num

    return result


def sol2(n: int, k: int, order: Iterable[int]) -> int:
    """빈도수가 아니라 출현 시기를 기준으로 다시 풀기"""
    order = list(order)
    plugs: set[int] = set()
    cnt = 0

    for idx, gadget_id in enumerate(order):
        plugs.add(gadget_id)

        if len(plugs) <= n:
            continue

        cnt += 1
        latest_used = find_latest_used(plugs, order[idx:])
        plugs.discard(latest_used)

    return cnt


if __name__ == "__main__":
    n, k = [int(x) for x in stdin.readline().split()]
    tmp_cnt: dict[int, int] = {}  # 임시로 occurrence를 측정하기 위해 사용하는 변수
    gadgetries: list[Gadgetry] = []

    answer = sol2(n, k, (int(x) for x in stdin.readline().split()))

    print(answer)
