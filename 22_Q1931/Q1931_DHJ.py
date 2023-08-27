#회의를 끝나는 시간 기준으로 정렬
#가장 빨리 끝나는 회의부터 시작한 후, 회의가 끝나고 나서 시작하는 다음 회의를 시작
import sys
input = sys.stdin.readline

N = int(input()) #N: 회의의 개수
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append([start, end])

meetings.sort(key=lambda x:(x[1], x[0])) #회의가 끝나는 시간을 기준으로 정렬 후, 회의가 시작하는 시간을 기준으로 정렬

schedule = []
schedule.append(meetings[0])

for i in range(1, len(meetings)):
    if meetings[i][0] < schedule[-1][1]:
        continue
    elif meetings[i][0] >= schedule[-1][1]:
        schedule.append(meetings[i])

print(len(schedule))