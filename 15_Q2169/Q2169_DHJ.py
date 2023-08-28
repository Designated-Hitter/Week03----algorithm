import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mars_map = []
for _ in range(N):
    mars = list(map(int, input().split()))
    mars_map.append(mars)

print(mars_map)
dp0 = [[0] * N for _ in range(M)] #방문 확인용 dp
dp1 = [[0] * N for _ in range(M)] #값 확인용 dp

print(dp0)
print(dp1)