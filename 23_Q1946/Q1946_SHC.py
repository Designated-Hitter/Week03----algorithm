"""
신입 사원
ref: https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1946-%EC%8B%A0%EC%9E%85%EC%82%AC%EC%9B%90-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
"""

from sys import stdin


input = stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    ls = sorted((tuple(int(x) for x in input().split()) for _ in range(n)), key=lambda x: x[0])
    hired = 1  # 적어도 서류에서 1등한 사람은 합격임

    best = ls[0][1]  # 서류1등의 면접점수를 가지고 비교
    for j in range(1, n):
        if ls[j][1] < best:
            best = ls[j][1]
            hired += 1
    print(hired)
