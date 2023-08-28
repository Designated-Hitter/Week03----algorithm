'''
    [효율성]
    - 메모리: 31256KB	
    - 시간: 44ms
'''
n,chu_lst = int(input()),list(map(int,input().split()))
m,check_chu_lst = int(input()),list(map(int,input().split()))

dp = [ 0 ]
for chu in chu_lst:
    # print(f'chu: {chu}')
    tmp=[]
    for i in dp:
        tmp.append(i+chu)
        tmp.append(abs(i-chu))
        # print(f'tmp: {tmp}')

    dp = list(set((dp + tmp)))
    # print(f'dp: {dp}')
    # print()

for chu in check_chu_lst:
    print('Y' if chu in dp else 'N',end=' ')
