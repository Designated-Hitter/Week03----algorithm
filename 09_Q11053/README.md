# 최적화 방법론 (not dp)

위의 방법을 활용하면 매 이터레이션마다 접근하게 되는 부분문제의 수가 N개가 된다. 만약 이를 줄일 수 있다면? 우리는 고정된 길이 i에서의 LIS의 길이를 가지고는 있으나, 그것 말고는 저장하고 있는 정보가 없다. 따라서 조금 더 영리하게 문제를 풀기 위해선 dp의 정의였던 **부분문제의 유일성** 을 포기 하고서라도 캐시를 말 그대로 동적으로 활용해야 한다.

[가장 긴 증가하는 부분 수열 (Longest Increasing Subsequence)](https://seungkwan.tistory.com/8)

> 💡 cache[i] = i 길이 증가수열의 마지막 원소 중 가장 작은 값을 가리키는 인덱스

```cpp
int efficient_lis(const vector<int>& seq)
{
    int L = 0, newL;
    memset(cache, 0, sizeof(cache));

    // cache[0]은 사용하지 않는다는 것을 염두하세요.
    for(size_t i = 0; i < seq.size(); i++)
    {
        // seq[i] > seq[m[j]]를 만족하는 가장 큰 j를 찾는다.
        int lo=1, hi=L;
        while (lo<=hi)
        {
            int mid = (lo+hi) / 2;
            if (seq[i] > seq[cache[mid]])
                lo = mid+1;
            else
                hi = mid-1;
        }
        newL = lo;
        cache[newL] = i;
        if (newL > L)
            L = newL;
    }

    return L;
}
```

위키피디아의 코드와 seungkwan 님의 코드를 적당히 섞어서 코드를 작성해 보았다. 위키피디아의 경우 cache 배열에 seq의 인덱스를 가리키게 만들어서 해석하기 매우 어려웠다. 하지만 lower bound를 찾는 과정이 드러나있어서 도움이 되었다.

결국 코드의 목표는 seq[cache] 배열을 계속 정렬된 상태로 만드는 것이다. 매 i마다 seq[cache] 배열의 seq[i]에 대한 lower bound를 이진탐색으로 찾아 다음 두 가지 행동 중 하나를 수행하게 된다.

1. cache 원소와 교체한다.
2. cache 맨 뒤에 i를 추가한다.

i 순회가 완료되고나면 현재 seq 배열의 마지막 값을 가리키고 있는 L이 곧 LIS의 길이가 된다.

아래는 임의의 seq : [2,10,6,14,1,9,15,13]에 대한 cache가 가지는 값의 변화에 대한 기록이다.

| i | seq | seq[cache[1..N]] | L |
| --- | --- | --- | --- |
| 0 | 2 | 2 | 1 |
| 1 | 10 | 2, 10 | 2 |
| 2 | 6 | 2, 6 | 2 |
| 3 | 14 | 2, 6, 14 | 3 |
| 4 | 1 | 1, 6, 14 | 0 |
| 5 | 9 | 1, 6, 9 | 3 |
| 6 | 15 | 1, 6, 9, 15 | 4 |
| 7 | 13 | 1, 6, 9, 13 | 4 |

# Pseudocode with python

C++에 `std::lower_bound`가 있다면 Python에는 [`bisect.bisect_left`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left)가 있다.

```python
from bisect import bisect_left


def length_of_lis(nums: list):
    """lower bound를 활용한 효율적인 캐시 검색"""
    cache = []

    for num in nums:
        newL = bisect_left(cache, num)
        if len(cache) == newL:
            cache.append(num)
        else:
            cache[newL] = num

    return len(cache)


assert 5 == length_of_lis([1, 2, 3, 4, 5])
assert 1 == length_of_lis([5, 4, 3, 2, 1])
assert 4 == length_of_lis([10, 9, 2, 5, 3, 7, 101, 18])
assert 2 == length_of_lis([4, 5, 2, 3, 1, 2])
assert 4 == length_of_lis([2, 10, 6, 14, 1, 9, 15, 13])
```
