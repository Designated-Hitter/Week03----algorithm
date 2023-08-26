#dp 리스트에 저장해야 할 것: 각 배열까지 도착했을 때 만들 수 있는 가장 긴 증가하는 수열
import sys
input = sys.stdin.readline

A = int(input())
B = list(map(int, input().split()))

dp = [0] * (A)

for i in range(1, A):
    for j in range(i):
        if B[i] > B[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))