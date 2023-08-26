# 04_Q2624

## SHC

첫번째 생각한 방법: 동전 2 문제와 동일하게 생각함.

```
f(n) = f(n-coin)+1 + f(n-1)
```

문제: 이거는 경우의 수를 찾는 문제인거지, 동전의 개수를 최소화 하는 문제가 아니었단 것이다.

그래서 [다음 블로그](https://mygumi.tistory.com/254)글을 읽어보았는데도 이해가 전혀 되지 않았다.

```python
dp[n][k] = sum(dp[n - (value * count)][k-1] for value, count in coins) # where coins = list[tuple[int, int]]
```

새로운 아침, 새로운 마음으로 다시 접근해보자. n원을 k개의 동전으로 만드는 경우의 수가 `dp[n][k]`로 부르자고 했다. 그리고 시작조건인 `dp[0][0] = 1`, `dp[1][0] = 0`, ... `dp[n][0] = 0` 이다.

이제 점화식을 제대로 해석해보자. 모든 코인들에는 각각 값 `value`와 수량 `count`가 제공된다. 따라서 수량을 넘는 조건에 대해서는 경우의 수가 0이 되겠지. `dp[n][k]`에 대해서 임의의 동전 `C = value, count`을 꼭 사용하여 dp를 채우고 싶다. 그래서 해당 동전의 `value * count` 만큼을 뺀 `n - (value * count)`값어치를 `k-1`개의 동전으로 만들었을 때의 그 경우의 수만큼 그대로 더해주는 것이다.

`C`도 순회하지만, `count`도 순회한다는 사실을 잊지말자. 나는 `remain` 배열을 따로 두어 계산했는데, 굳이 그럴 필요가 없었다.

---

블로그 글을 잘못 읽었다. `dp[n][k]`는 n원을 만들기 위해 k번째 동전까지 사용해서 구할 수 있는 경우의 수였다. 그리고 `dp[n - (v * c)][k - 1]`의 뜻은 다음 동전까지 써서 n원을 만들 수 있는 경우의 수를 의미한다. 아래 예시에서 k는 0부터 각각 1원짜리 5개, 5월짜리 3개, 10원짜리 2개를 의미한다.

|n\k|0|1|2|
|-|-|-|-|
|0|1|1|1|
|1|1|1|1|
|2|1|1|1|
|3|1|1|1|
|4|1|1|1|
|5|1|2|1|
|6|0|1|1|
|7|0|1|1|
|8|0|1|1|
|9|0|1|1|
|10|0|2|3|
|11|0|1|2|
|12|0|1|2|
|13|0|1|2|
|14|0|1|2|
|15|0|2|4|
|16|0|1|2|
|17|0|1|2|
|18|0|1|2|
|19|0|1|2|
|20|0|1|4|

그래서 블로그에서 나온 점화식이 드디어 말이 된다.예를 들어 `dp[10]`쪽을 보자. 1원 5개만 가지고는 10원을 만들 수 없으니 `dp[10][0] = 0`이다. 반면에 5원짜리 동전을 0개 사용해서 만들 수 있는 경우의 수 + 1개 사용했을 때 + 2개 사용했을 때 만들 수 있는 경우의 수는 각각 `dp[10][0] + dp[5][0] + dp[0][0] = 0 + 1 + 1` 이므로 2가 된다. 마지막으로 10원짜리 동전을 0개 사용했을 때, 1개 사용했을때를 각각 보자면 `dp[10][1] + dp[0][1] = 2 + 1` 이므로 3이 된다.