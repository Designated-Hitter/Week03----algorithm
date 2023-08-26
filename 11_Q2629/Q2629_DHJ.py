#dp 리스트에서 기억해야 할 값: 0 <= 무게 <= 모든 추의 합 사이의 범위에서 각 무게를 측정 가능한지에 대한 여부

import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split())) #오름차순으로 이미 정렬된 값
print(weights)
target_N = int(input())
target_weights = list(map(int, input().split()))
print(target_weights)

maximum_weight = sum(weights)

dp = [0] * (maximum_weight + 1)
dp[0] = 1
dp [-1] = 1