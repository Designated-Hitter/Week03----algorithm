'''
    [효율성]
    - 메모리: 31256KB	
    - 시간: 152ms
'''
n = int(input())

ls = [0]
ls.extend(list(map(int, input().split())))

dp = [0] * (n+1)

for i in range(1, n+1):
    maxi = 0
    for j in range(0, i):
        # ls[i] 보다 작은 값
        if ls[i] > ls[j]:
            # 중에서 가장 큰 값
            maxi = max(maxi, dp[j])
    dp[i] = maxi + 1

print(max(dp))