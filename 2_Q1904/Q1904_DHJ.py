#문제의 핵심: d[n] = d[n-2] + d[n-1]
#나머지를 구할 때, dp[k]를 다 구해놓고 나머지를 구하려고 하면 오류가 나옴
#dp[n]을 구할때 마다 미리 나눠놔야 문제가 없다 
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3, N + 1):
    dp[k] = (dp[k-1] + dp[k-2]) % 15746

print(dp[N])