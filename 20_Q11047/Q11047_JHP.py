'''
    [효율성]
    - 메모리: 31256KB	
    - 시간: 40ms
'''
n, k = map(int, input().split())
money = []

for _ in range(n):
    coin = int(input())
    money.append(coin)

money.sort(reverse=True)

ans = 0
for i in money:
    ans += k // i
    k = k % i


print(ans)
