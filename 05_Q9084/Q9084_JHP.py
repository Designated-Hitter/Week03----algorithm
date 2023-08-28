'''
    [효율성]
    - 메모리: 31256KB	
    - 시간: 92ms
'''

# 주어진 금액을 세는 모든 방법

t = int(input())
for _ in range(t):
    # n = 2
    n = int(input())
    # [1, 2]
    coins = list(map(int, input().split()))
    # 1000
    k = int(input())
    # ex) dp[1001], 0으로 초기화
    dp = [0] * (k+1)
    dp[0] = 1

    # 1, 2 [1, 2]
    for coin in coins:
        # 1 ~ 1000
        for j in range(1, k+1):
            # [1, 1000] - [1, 2]
            if j-coin >= 0:
                # dp[1] ~ dp[1000] += dp[]
                dp[j] += dp[j-coin]
            print(dp)

    print(dp[k])