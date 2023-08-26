import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #N = 물품의 수, K=무게 제한
for _ in range(N):
    W, V = map(int, input().split()) #W = 각 물건의 무게, V = 해당 물건의 가치
