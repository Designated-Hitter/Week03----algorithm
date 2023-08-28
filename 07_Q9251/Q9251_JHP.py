'''
    [효율성]
    - 메모리: 56440KB	
    - 시간: 580ms
'''

x = list(input())
y = list(input())
m = len(x)
n = len(y)

dp = [[0 for j in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if x[i-1] == y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[m][n])