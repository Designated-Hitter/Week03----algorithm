'''
    [효율성]
    - 메모리: 219092KB	
    - 시간: 5940ms
'''
import sys

input = sys.stdin.readline

# 테스트 케이스
t = int(input())

# 테스트 케이스 수 만큼 반복
for _ in range(t):
    # 채용 인원
    cnt = 0
    # 순위!
    ls = []
    # 이번 케이스에 확인할 사람 수
    n = int(input())
    
    for i in range(n):
        ls.append(list(map(int, input().split())))
    ls.sort()

    mini = n + 1
    cnt = 0
    for first, second in ls:
        if second < mini:
            mini = second
            cnt += 1

    print(cnt)