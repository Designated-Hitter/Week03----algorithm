'''
    [효율성]
    - 메모리: 115272KB	
    - 시간: 180ms
'''
n, k = map(int, input().split())

dp = [0] * (k+1)
for _ in range(n):
    w, v = map(int, input().split())
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])
