#냅색 알고리즘, 배낭 문제라는 이름으로 유명한 문제라고 함
#담을 수 있는 물건이 나누어질 때(설탕 300g 등): 분할가능 배낭문제
#담을 수 있냐 없냐 로만 판단할 때: 0-1 배낭문제
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #N = 물품의 수, K=무게 제한
dp = [[0]*(K+1) for _ in range(N+1)] #dp[i][j]: 처음부터 i까지의 물건을 살펴보고, 배낭의 용량이 j였을 때 배낭에 들어간 물건의 가치합의 최대값
weights = [0]
values = [0]
for _ in range(N):
    W, V = map(int, input().split()) #W = 각 물건의 무게, V = 해당 물건의 가치
    weights.append(W)
    values.append(V)

for i in range(1, N+1): #i번째 물건
    for j in range(1, K+1): #배낭 용량 j
        if j < weights[i]: #배낭 용량이 넣을 물건 무게보다 더 작아서 안 들어간다
            dp[i][j] = dp[i-1][j] 
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i]) 

print(dp[N][K])
