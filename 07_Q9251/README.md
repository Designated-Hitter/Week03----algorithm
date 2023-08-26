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
