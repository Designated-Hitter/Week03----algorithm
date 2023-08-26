#팰린드롬 = 회문 1234321
#DP를 어떻게 적용할 수 있을 지 감이 안 와서 반복문으로만 짜봄
#예제는 통과하지만 문제는 시간초과

#----------------

#팰린드롬이 될 조건 양 끝 숫자가 같고 (i번 == j번), 그 사이의 숫자가(dp[i+1][j-1]) 팰린드롬이라면 팰린드롬 
import sys
input = sys.stdin.readline

N = int(input()) #수열의 크기
num_list = list(map(int, input().split()))
dp=[[0] * N for _ in range(N)] #N*N의 2차원배열

for i in range(N):
    dp[i][i] = 1 #1글자 뿐이라면 회문판정

for i in range(N - 1):
    if num_list[i] == num_list[i+1]: #연속된 2글자가 같다면 회문판정
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

for count in range(N - 2): #3글자 이상인 경우
    for i in range(N - 2 - count):
        j = i + 2 + count
        if num_list[i] == num_list[j] and dp[i+1][j-1] == 1: #양 끝 숫자가 같고, 그 안의 숫자들이 팰린드롬인가?
            dp[i][j] = 1


M = int(input()) #질문의 개수

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])

# for _ in range(M):
#     S, E = map(int, input().split())
#     sliced = num_list[S:E + 1]
#     if len(sliced) == 1: #1글자 뿐이라면
#         print(1)         #회문 판정
#     elif len(sliced) == 2:          #2글자라면
#         if sliced[0] == sliced[1]:  #둘이 같을때만 회문 판정
#             print(1)
#         else:
#             print(0)             
#     else:
#         R = len(sliced) // 2 #잘라낸 list를 2로 나눈 몫
#         for i in range(1, R + 1):
#             if sliced[i - 1] != sliced[-1*i]:
#                 print(0)
#                 break
#             else:
#                 print(1)