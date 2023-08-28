import sys
input = sys.stdin.readline

N = int(input()) #N: 도시의 수
cost_list = [[0] * (N + 1)]
for _ in range(N):
    cost = [0] + list(map(int, input().split()))
    cost_list.append(cost)

print(cost_list)

dp = [[0] * (N + 1) for _ in range(N + 1)]

print(dp)