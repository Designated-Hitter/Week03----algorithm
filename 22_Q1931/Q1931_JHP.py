'''
    [효율성]
    - 메모리: 134228KB	
    - 시간: 468ms
'''
import sys

input = sys.stdin.readline
t = int(input())
time = []

for _ in range(t):
    time.append(list(map(int, input().split())))

# 끝나는 시간(end)이 같을수 있음!
time.sort(key=lambda x: (x[1], x[0]))

c = 0
cnt = 0
for start, end in time:
    if start >= c:
        cnt += 1
        c = end

print(cnt)


