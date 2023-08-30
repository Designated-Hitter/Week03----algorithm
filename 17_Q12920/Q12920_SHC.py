"""
평범한 배낭 2
ref: https://blog.koderpark.dev/171
"""

from sys import stdin

input = stdin.readline
MAXN = 100
MAXK = 10_000

w = []  # weights
v = []  # values

n, m = (int(x) for x in input().split())

for a, b, c in ((int(x) for x in input().split()) for _ in range(n)):
    # (a, b, c) = (무게, 만족도, 개수)
    j = 0
    while c > 0:
        # 모든 숫자는 2진수로 표현이 가능하다는 점 => C개를 고르는 경우의 수에 대해서 두 이진수의 합으로 구성을 하게되면
        # 같은 연산의 결과를 중복계산하는 일을 사전에 방지할 수 있다.
        # 예를 들어, 5 = 1 + 4 = 2 + 3 = 5 이렇게 여러가지 방법으로 표현할 수 있기 때문에 타임아웃이 발생할 우려가
        # 있지만 5 = (1 << 0) + (1 << 2) 이렇게 본다면 5를 표현할 수 있는 방법이 단 한가지로 압축이 된다.
        tmp = min(1 << j, c)  # overflow 방지
        w.append(a * tmp)
        v.append(b * tmp)
        c -= tmp
        j += 1


# dp[n][k] = n번째 물건까지 살펴보았을 때, 무게가 k인 배낭의 최대 가치
dp = [[0 for _ in range(MAXK + 1)] for _ in range(len(w) + 1)]

for i in range(1, len(w) + 1):
    for j in range(1, m + 1):
        if j >= w[i - 1]:
            dp[i][j] = max(dp[i - 1][j - w[i - 1]] + v[i - 1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[len(w)][m])
