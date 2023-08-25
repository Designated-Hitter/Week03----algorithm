import sys
input = sys.stdin.readline

X = list(input().rstrip())
Y = list(input().rstrip())

def lcs (x, y):
    x, y = [' '] + x, [' '] + y #계산에 도움이 되도록 0번 인덱스에 빈 칸 추가
    m, n  = len(x), len(y)
    c = [[(0,0) for _ in range(n)] for _ in range(m)] #계산을 기록할 2차원 배열

    for length_i, position_i in range(1, m):
        for length_j, position_j in range(1, n):
            if x[length_i] == y[length_j]:
                c[length_i][length_j] = (c[length_i-1][length_j-1] + 1 , 1)
            else:
                c[length_i][length_j] = max(c[length_i][length_j-1], c[length_i-1][length_j])
