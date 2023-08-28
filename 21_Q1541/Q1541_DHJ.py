#- 연산자 뒤에 +연산자가 오는 경우가 가장 값이 작아지므로 - 연산자 기준으로 계산식을 나눔
#+ 연산자를 기준으로 나뉘는 숫자들을 더한 후, -계산을 수행함 
import sys
input = sys.stdin.readline

minus_split = input().split('-')

plus_list = []

for i in minus_split:
    sum = 0
    temp = i.split('+')
    for j in temp:
        sum += int(j)
    plus_list.append(sum)

n = plus_list[0]
for i in range(1, len(plus_list)):
    n -= plus_list[i]

print(n)