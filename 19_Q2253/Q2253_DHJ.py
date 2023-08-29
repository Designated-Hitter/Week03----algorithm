#dp에 저장해야 할 값 = 각 칸에 도착하기 위해 필요한 최소한의 점프 횟수
#그러나 각 돌에 어떤 속도로 도달하냐에 따라서 다음 돌에 도착하는 횟수 역시 달라지며, 그 속도 때문에 마지막 돌에 못 가는 경우 역시 생기므로
#dp는 각 돌에 도착하기 위한 최소한의 점프 횟수 + 그 돌에 도착했을 때의 속도 역시 기록하는 2차원 리스트가 되어야 함

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #N: 돌의 개수, M: 크기가 작아서 밟을 수 없는 돌의 개수
small_stones = []
for _ in range(M):
    small_stone = int(input())
    small_stones.append(small_stone)

dp = [[float('inf')] * (int((2*N)**0.5) + 2) for _ in range(N + 1)]
#(2*N) ** 0.5) + 1은 첫째항이 1이고 공차가 1인 등차수열에서 수열의 합이 N이 될 때 마지막 항의 근사값, 즉 돌의 갯수가 N개일 때 나올 수 있는 속도의 최대값에 가까운 값
#최대 속도의 정확한 값이 필요한 것이 아니라 이 이상 넘어설 수 없는 최대값을 (계산하기 더 편하게 정수로) 대충이나마 설정하는 것이 더 중요하기 때문에 정확한 값보다 더 큰 근사값을 설정
dp[1][0] = 0

for i in range(2, N + 1):
    if i in small_stones:
        continue
    for j in range(1, int((2*i)**0.5) + 1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1
#점화식: i라는 점에 j라는 속도로 도달했을 때 최소 점프 횟수는 i-j의 위치에 따라 (각각 j-1, j, j+1의 속도로 도달했을 때 시행한 점프) + 1
if min(dp[N]) == float('inf'): #목표지점까지 갈 수 없음
    print(-1)
else:
    print(min(dp[N])) #dp[N]은 각각의 속도로 N에 도착했을 때 얻을 수 있는 점프의 여러 값들이 배열로 구성되어 있는데, 그 중 최소값을 출력