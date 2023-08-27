"""
가장 긴 증가하는 부분 수열
"""

from bisect import bisect_left
from sys import stdin


def lis(nums: list):
    """lower_bound를 이용한 효율적인 캐시 탐색
    어차피 LIS는 항상 정렬되어있다는 점을 응용한 것이다.
    """
    cache = []

    for num in nums:
        j = bisect_left(cache, num)
        if len(cache) == j:
            cache.append(num)
        else:
            cache[j] = num
    return len(cache)


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    nums = [int(x) for x in stdin.readline().split()]
    print(lis(nums))
