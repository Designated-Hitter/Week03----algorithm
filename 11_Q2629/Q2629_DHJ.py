#dp 리스트에서 기억해야 할 값: 0 <= 무게 <= 모든 추의 합 사이의 범위에서 각 무게를 측정 가능한지에 대한 여부

import sys
input = sys.stdin.readline

N = int(input()) #추의 개수 <= 30
weights = list(map(int, input().split())) #오름차순으로 이미 정렬된 추의 무게값 <= 500
# print(weights)
target_N = int(input()) #무게를 재야하는 구슬의 개수
target_weights = list(map(int, input().split())) #구슬의 무게
# print(target_weights)

maximum_weight = sum(weights)

dp = [[0] * ((30 * 500) + 1) for _ in range(N + 1)] #dp[i][j] == i 번째까지의 추를 놓았을 때, j무게를 만들 수 있는가

result = set()

#weights = 추의 리스트
#N = 전체 추의 개수
#now = 이제 올려놓을 추의 index
#left = 왼쪽 팔의 무게
#right = 오른쪽 팔의 무게

def libra(weights, N, now, left, right):
    new = abs(left - right) #처음 함수가 호출되었을 때 무게를 잼

    if new not in result: #new가 처음 재는 무게라면
        result.add(new) #result에 추가

    if now == N: #재귀 탈출 조건
        return 0
    
    if dp[now][new] == 0: #now까지의 추로 아직 무게를 잰 적이 없다면
        libra(weights, N, now + 1, left + weights[now], right) #왼쪽에 놓기
        libra(weights, N, now + 1, left, right + weights[now]) #오른쪽에 놓기
        libra(weights, N, now + 1, left, right) #놓지 않기
        dp[now][new] = 1 #무게를 쟀다고 표시

libra(weights, N, 0, 0, 0)
answer = []

for target_weight in target_weights:
    if target_weight in result:
        answer.append('Y')
    else:
        answer.append('N')

print(*answer)