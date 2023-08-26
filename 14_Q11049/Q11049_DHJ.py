#dp에 저장해야 할 값: 행렬 3개를 곱한 곱셈 연산의 최소값
import sys
input = sys.stdin.readline

N = int(input()) #행렬의 개수
matrix_list = []

for _ in range(N):
    r, c = map(int, input().split())
    matrix_list.append([r, c])


dp = [[0] * N for i in range(N)] #dp에 저장되는 값: i번 숫자로 시작해서 j번 숫자로 끝나는 행렬의 최소 곱셈 연산 횟수 값

for count in range(N-1):
    for i in range(N-1-count):
        j = i + count + 1
        dp[i][j] = 2**31 #문제에 제시된 나올 수 있는 최대 값
        for k in range(i, j): #i <= k <= j
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix_list[i][0] * matrix_list[k][1] * matrix_list[j][1])

print(dp[0][-1])