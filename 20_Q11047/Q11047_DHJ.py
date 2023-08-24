import sys
input = sys.stdin.readline

N, K = map(int, input().split())

purse = []
for i in range(N):
    coin = int(input())
    purse.append(coin)
count = 0

purse.reverse()

while K > 0:
    for coin in purse:
        if coin > K:
            continue
        else:
            r = (K // coin)
            count += r
            K = K - (coin * r)

print(count)