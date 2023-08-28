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

print(small_stones)
dp = [[sys.maxsize] * N for _ in range(N)]

print(dp)
