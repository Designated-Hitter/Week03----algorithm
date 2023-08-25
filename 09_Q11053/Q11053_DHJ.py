import sys
input = sys.stdin.readline

A = int(input())
B = [0] + list(map(int, input().split()))
print(B)
dp = [0] * (A + 1)

for i in range(1, B - 1):
    max = B[i]
    
    if B[i + 1] > max:
        max = B[i + 1]
        dp[i] =  dp[i] + 1



