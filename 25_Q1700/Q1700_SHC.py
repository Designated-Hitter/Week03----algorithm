"""
멀티탭 스케쥴링
"""

from dataclasses import dataclass
from functools import total_ordering
from heapq import heapify, heappop, heappush
from sys import stdin
from typing import Self

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


if __name__ == "__main__":
    n, k = [int(x) for x in stdin.readline().split()]
    tmp_cnt: dict[int, int] = {}  # 임시로 occurrence를 측정하기 위해 사용하는 변수
    gadgetries: list[Gadgetry] = []

    for idx, gadget_id in enumerate(int(x) for x in stdin.readline().split()):
        if gadget_id not in tmp_cnt:
            tmp_cnt[gadget_id] = idx
        if tmp_cnt[gadget_id] < idx:
            gadgetries.append(Gadgetry(gadget_id, idx - tmp_cnt[gadget_id]))
        tmp_cnt[gadget_id] = idx

    # Infinities
    for gadget_id in tmp_cnt.keys():
        gadgetries.append(Gadgetry(gadget_id, INF))

    maxheap: list[Gadgetry] = []
    cnt = 0
    for gadget in gadgetries:
        if len(maxheap) > n - 1:
            is_updated = False
            for i in range(len(maxheap)):
                if maxheap[i] == gadget:
                    maxheap[i] = gadget
                    is_updated = True
                    heapify(maxheap)
                    break
            if is_updated:
                continue
            cnt += 1
            heappop(maxheap)
        heappush(maxheap, gadget)

    print(cnt)
