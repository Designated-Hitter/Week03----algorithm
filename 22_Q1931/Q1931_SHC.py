"""
회의실 배정
ref: https://hongcoding.tistory.com/22

종료시간이 빠르게 끝날수록 이득, 시작시간으로 정렬 후 종료시간이 짧은 순서대로 구하면 된다. 
"""

from sys import stdin


input = stdin.readline

n = int(input().strip())
room = sorted((tuple(int(x) for x in input().split()) for _ in range(n)), key=lambda x: x[0])
room.sort(key=lambda x: x[1])

cnt = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)
