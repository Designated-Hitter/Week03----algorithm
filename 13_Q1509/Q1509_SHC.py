"""
펠린드롬 분할
ref: https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80

길이 1, 2짜리 펠린드롬을 만들어준다. 3 이상짜리부터 펠린드롬? 문제처럼 똑같이 접근하면 된다.
"""

from sys import stdin


input = stdin.readline

S = input().strip()
L = len(S)
MAXL = 2500

dp = [MAXL for _ in range(L + 1)]
dp[-1] = 0
is_p = [[False for _ in range(L)] for _ in range(L)]

for i in range(L):
    # 길이 1짜리 팰린드롬
    is_p[i][i] = True

for i in range(1, L):
    # 길이 2짜리 팰린드롬
    if S[i - 1] == S[i]:
        is_p[i - 1][i] = True

for l in range(3, L + 1):
    for start in range(L - l + 1):
        # 길이 3 이상인 팰린드롬
        end = start + l - 1
        if S[start] == S[end] and is_p[start + 1][end - 1]:
            is_p[start][end] = True

for end in range(L):
    for start in range(end + 1):
        # 최소 팰린드롬 분할의 개수를 세 달랬으니까..
        if is_p[start][end]:
            # REVIEW -  이놈의 의미가 뭔지 모르겠다.
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            # REVIEW -  이놈의 의미가 뭔지 모르겠다.
            dp[end] = min(dp[end], dp[end - 1] + 1)

print(dp[L - 1])
