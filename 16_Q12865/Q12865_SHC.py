"""
평범한 배낭
ref: https://hongcoding.tistory.com/50
"""

from sys import stdin


input = stdin.readline

n, k = [int(x) for x in input().split()]

thing: list[tuple[int, int]] = [(int(0), int(0))] + [
    tuple(int(x) for x in input().split()) for _ in range(n)
]

# dp[n][k] = n번째 물건까지 살펴보았을 때, 무게가 K인 배낭의 최대 가치
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            # 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않고 이전의 선택을 복제한다.
            dp[i][j] = dp[i - 1][j]
        else:
            # 두 선택지 중 더 나은 가치를 선택한다.
            # 1. 현재 넣을 물건의 무게만큼 배낭에서 빼낸 뒤 해당 물건을 채워넣는다.
            # 2. 현재 물건을 넣지 않고 이전의 선택을 고수한다.
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
