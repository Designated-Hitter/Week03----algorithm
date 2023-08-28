'''
    [효율성]
    - 메모리: 56708KB	
    - 시간: 548ms
'''
import sys
sys.setrecursionlimit(10**6)

x = list(input())
y = list(input())
m = len(x)
n = len(y)

dp = [[0 for j in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if x[i-1] == y[j-1]: # 0번째 인덱스부터 글자를 비교
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

res = dp[m][n]

ans = []
def find_text(r, c):
    if r == 0 or c == 0:
        return
    
    if x[r-1] == y[c-1]:
        ans.append(x[r-1])
        find_text(r-1, c-1)
    
    else:
        if dp[r-1][c] > dp[r][c-1]:
            find_text(r-1, c)
        else:
            find_text(r, c-1)

if res == 0:
    print(0)
else:
    find_text(m, n)
    print(res)
    print(''.join(ans[::-1]))