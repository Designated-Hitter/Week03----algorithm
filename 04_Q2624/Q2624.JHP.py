'''
    [효율성]
    - 메모리: 115268KB	
    - 시간: 216ms
'''

import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]
dp = [0] * (T + 1)
dp[0] = 1
 
# for (5, 3) in [(5, 3), (10, 2), (1, 5)]
for p, n in coins:

    # [20 ~ 1], 0은 1로 초기화
    # 단, 금액을 오름차순으로 채우면 이미 해당 동전으로 이전에 계산이 된 테이블에 대해 중복으로 계산이 되므로
    # 큰 금액부터 내림차순으로 테이블을 채워가도록 한다.
    for t in range(T, 0, -1):
        # 동전 갯수 ex) 5원은 3개 즉,  
        for i in range(1, n + 1):
            if t - (p * i) >= 0:
                dp[t] += dp[t - (p * i)]
 
print(dp[T])



#   [20 - (5 * 1)], [20 - (5 * 2)], [20 - (5 * 3)]
#   [15]              [10]               [5]

#   [20 - (1 * 1)], [20 - (1 * 2)], [20 - (1 * 3)], [20 - (1 * 4)], [20 - (1 * 5)], 
#   [19]                [18]            [17]            [16]            [15]


