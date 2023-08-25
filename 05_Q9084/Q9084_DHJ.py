#dp테이블에서 기억해야 하는 것: 금액 n을 동전으로 교환하는 방법의 수

import sys
input = sys.stdin.readline

T = int(input()) #테스트 케이스
for _ in range(T):
    N = int(input()) #동전의 가지수
    coins = list(map(int, input().split()))

    M = int(input()) #만들어야 할 금액
    dp = [0] * (M + 1)
    dp[0] = 1 #어떤 동전도 사용하지 않는 방법 하나
    for coin in coins:
        for i in range(1, M + 1): #1원부터 M원 까지
            if i >= coin:
                dp[i] += dp[i-coin] #i원을 만드는 방법은 i-coin원을 만드는 방법
    print(dp[M])

#메모리: 31256 KB
#시간: 84 ms