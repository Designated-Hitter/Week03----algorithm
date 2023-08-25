import sys
input = sys.stdin.readline

X = list(input().rstrip())
Y = list(input().rstrip())
result = []

def lcs (x, y):
    x, y = [' '] + x, [' '] + y #계산에 도움이 되도록 0번 인덱스에 빈 칸 추가
    m, n  = len(x), len(y)
    c = [[0 for _ in range(n)] for _ in range(m)] #계산을 기록할 2차원 배열
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])

    return print(c[-1][-1])

lcs(X, Y)

answer = []



