# 06_Q2294 동전 2

## SHC

[지난주에](https://github.com/ChoiWheatley/swjungle-week-02/blob/71057bb44e831ecd4691d061a4ff66d31e7c881d/ChoiWheatley/p2294.py#L4) DP로 풀었다. 점화식은 다음과 같다.

```python
dp[i] = min(dp[i], dp[i - coin] + 1) # where `i` is cost, `coin` is value of each coin
```