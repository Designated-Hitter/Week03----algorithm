#dp list에서 기억해야 할 것: i원을 만드는데 필요한 동전의 개수의 최소값
import sys

input = sys.stdin.readline

n, k = map(int, input().split()) #n = 동전의 종류, k = 만들려고 하는 가치
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))
coins.sort()

dp = [10001] * (k + 1) # 0 <= k <= 10000이니까
dp[0] = 0 #0원을 만드는 데에 필요한 동전의 개수 0개

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1) #기존값과 이전 요소 + 1 값을 비교
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])