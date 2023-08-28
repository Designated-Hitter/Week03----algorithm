'''
    [효율성]
    - 메모리: 114488KB	
    - 시간: 152ms
'''
# k원을 만족하는 최소 개수

n, k = map(int, input().split())
coins = set()
for _ in range(n):
    coins.add(int(input()))

coins = sorted(list(coins))
init = k+1
dp = [k+1] * (k+1)

# 코인 안써도 됨
dp[0] = 0

for coin in coins:
    for j in range(1, k+1):
        if j-coin >= 0:
            dp[j] = min(dp[j], dp[j-coin]+1)
    print(dp)
if dp[k] > k:
    print(-1)
else:
    print(dp[k])