'''
    [효율성]
    - 메모리: 61972KB	
    - 시간: 2152ms
'''
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())

num.insert(0, 0)

# print(f'dp: {dp}') # (n+1) x (n+1) -> 초기화
dp = [[0]*(n+1) for _ in range(n+1)]

# print(f'num: {num}') # 입력 받은 숫자


# n = 7
# i = [1, 2, 3, 4, 5, 6, 7]
for i in range(1, n+1):

    # i = 0, j = [0] # 출력 x

    # i = 1, j = [1] # dp[1][1] == 1
    # i = 2, j = [1, 2] # dp[2][1] = [ num[1](1) != num[2](2) ], dp[2][2] = [ num[2](2) == num[2](2) ]
    # i = 3, j = [1, 2, 3] # dp[3][1] = [ num[3](1) == num[1](1) ], dp[3][2] = [ num[3](1) != num[2](2) ], dp[3][3] = [ num[3](1) != num[3](1) ], 
    # i = 4, j = [1, 2, 3, 4] # 


    for j in range(1, i+1):
        if i == j:
            # print(f'i == j : {i}, {j}')
            dp[i][j] = 1

        # 두글자 -> num[i] == num[j] 같으면 펠린드롬
        if i-j == 1 and num[i] == num[j]:
            # print(f'i-j == 1 : {i}, {j}')
            dp[i][j] = 1
        
        # ex) 4-2, 세글자 이상 and 
        if i-j >= 2 and num[i] == num[j] and dp[i-1][j+1] == 1:
            # print(f'i-j >= 2 : {i}, {j}')
            dp[i][j] = 1

    # for i in dp:
    #     print(i)
    # print()

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[e][s])

'''
### 풀이 방법
- `다이나믹프로그래밍`을 활용하여 해결하였다.
- DP[S][E] = S번째에서 E번째까지가 펠린드롬이면 1, 아니면 0으로 표기한다
- S번째에서 E번째까지가 펠린드롬이려면 먼저 DP[S+1][E-1] == 1이어야 하고, S번째 수와 E번째 수가 같아야 한다.
- 만약 |S-E| == 1 이면 두 수가 같은지만 확인하면 되고, S == E이면 항상 펠린드롬이다.
'''