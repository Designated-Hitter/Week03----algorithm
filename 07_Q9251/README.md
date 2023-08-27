# 07_Q9251 LCS

[참고: 누워서 보는 알고리즘 {Youtube}](https://youtu.be/z8KVLz9BFIo?si=fDh-h9IQF1Hj67hk)

최장공통부분수열의 길이를 구하는 문제.

부분수열의 정의: 수열 S에서 순서를 바꾸지 않고 임의의 원소를 꺼낸 모든 수열을 S의 부분수열이라고 부른다.

예:

```python
S = "Hello, World!"
possible_subsequence = [
    "Hello",
    "World",
    "Hold",
    "ello",
    ...
]
```

## SHC

1. 두 접두어가 같은 문자로 끝나는 경우 => `LCS(X[:-1], Y[:-1])`
2. 두 접두어가 다른 문자로 끝나는 경우 => `max(LCS(X[:-1], Y), LCS(X, Y[:-1]))`

### Recurrence Relation

재귀적 관계로 나타낸 수도코드는 다음과 같다.

```python
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
```

### Bottom-Up Style with memoization

아무래도 중복 부분문제 (Overlapping Subproblems)들이 자주 겹치다 보니 시간초과가 발생하게 되었다. 심지어 `@lru_cache(256)`, `@cache` 데코레이터를 사용하여도 각각 시간초과, 메모리 초과 에러가 발생하였다. 따라서 고전적인 방식 그대로 코드를 재작성했다. X와 Y 앞에 빈 공백 문자를 넣는다는게 바로 와닿지 않았다. 하지만 초기값을 지정하기 위한 방법이었던 것이고, 원치 않는다면 그냥 DP 공간을 1씩 넓힌 다음 X, Y 인덱싱 할 때 문자열 참조 인덱스를 1씩 줄이면 된다.

```python
def LCS(X: str, Y: str) -> int:
    """X와 Y의 최장 공통부분수열의 길이를 구한다."""
    # ∵ 빈 수열도 비교해야 하기 때문. (초기조건)
    X = " " + X
    Y = " " + Y
    dp = [[0 for _ in range(len(Y))] for _ in range(len(X))]
    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if X[i] == Y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

```

![LCS](../media/IMG_2714.jpg)
