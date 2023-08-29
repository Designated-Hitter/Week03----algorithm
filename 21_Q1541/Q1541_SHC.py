"""
잃어버린 괄호

ref: https://puleugo.tistory.com/29
"""

equation = input()
m = equation.split("-")

answer = 0

# 음수로 시작하는 케이스
x = sum(int(x) for x in m[0].split("+"))
if equation[0] == "-":
    answer -= x
else:
    answer += x

# 0번은 진행했으니까 1번째 인덱스부터
for subeq in m[1:]:
    answer -= sum(int(subsum) for subsum in subeq.split("+"))

print(answer)
