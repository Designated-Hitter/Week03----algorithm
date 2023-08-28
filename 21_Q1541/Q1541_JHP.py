'''
    [효율성]
    - 메모리: 31256KB	
    - 시간: 44ms
'''
# - 기호를 기준으로 자른다.
s = input().split('-')
num = []

# 자른 s를 + 기호를 기준으로 다시 자르고 ans 누적
for i in s:
    ans = 0
    tmp = i.split('+')
    for j in tmp:
        ans += int(j)

    # 새로운 리스트에 결과를 담고
    num.append(ans)
 
# 초기값은 0번째로 하고 다음 값부터 빼준다.
n = num[0]
for i in range(1, len(num)):
    n -= num[i]

print(n)