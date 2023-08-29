import sys
input = sys.stdin.readline
N, M = map(int, input().split()) #N: 물건 종류의 수, M: 민호가 들 수 있는 가방의 최대 무게
dp = [0 for _ in range(M + 1)]
weight = []
utility = []
for _ in range(N):
    V, C, K = map(int, input().split()) #V: 물건의 무게, C: 민호가 느끼는 효용, K:물건의 개수

    idx = 1
    while K > 0:
        tmp = min(idx, K)
        weight.append(V * tmp)
        utility.append(C * tmp)

        idx *= 2
        K -= tmp

for i in range(len(weight)):
    for j in range(M, 0, -1):
        if j >= weight[i]:
            dp[j] = max(dp[j], dp[j-weight[i]] + utility[i])