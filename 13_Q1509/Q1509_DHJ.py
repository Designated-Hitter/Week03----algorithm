import sys
input = sys.stdin.readline

str_list = input().rstrip()
L = len(str_list)
dp = [2500 for _ in range(L+1)] #2500 = 문자열의 최대 길이 = 가능한 팰린드롬 분할의 최대 길이
dp[-1] = 0
is_p = [[0 for j in range(L)] for i in range(L)] #is_p[i][j]는 i부터 j가 팰린드롬이라면 1, 아니면 0을 반환

for i in range(L): #길이 1짜리 팰린드롬
    is_p[i][i] = 1

for i in range(1,L): #길이 2짜리 팰린드롬
    if str_list[i-1] == str_list[i]:
        is_p[i-1][i] = 1

for k in range(3, L + 1): #길이 3이상 팰린드롬
    for start in range(L - k + 1):
        end = start + k - 1
        if str_list[start] == str_list[end] and is_p[start + 1][end - 1]:
            is_p[start][end] = 1

for end in range(L):
    for start in range(end + 1):
        if is_p[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            dp[end] = min(dp[end], dp[end - 1] + 1)

print(dp[L - 1])