#냅색 알고리즘, 배낭 문제라는 이름으로 유명한 문제라고 함
#담을 수 있는 물건이 나누어질 때(설탕 300g 등): 분할가능 배낭문제
#담을 수 있냐 없냐 로만 판단할 때: 0-1 배낭문제
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #N = 물품의 수, K=무게 제한
dp = [[0]*(K+1) for _ in range(N+1)]
things = [[0,0]]
for _ in range(N):
    W, V = map(int, input().split()) #W = 각 물건의 무게, V = 해당 물건의 가치
    things.append([W, V])

print(things)
