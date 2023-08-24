import sys
input = sys.stdin.readline

n = int(input())

def fibonacci_generator(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
answer = []
for num in fibonacci_generator(n):
    answer.append(num)
print(answer[-1])