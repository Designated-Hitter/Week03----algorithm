import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #N: 멀티탭 구멍의 개수, K: 전기용품의 총 사용횟수

elec_list = list(map(int, input().split()))
print(elec_list)

plug_list = [elec_list[i:i + N] for i in range(0, len(elec_list), N)]

print(plug_list)

count = 0
for i in range(len(plug_list) - 1):
    print(f'i = {i}')
    for j in range(len(plug_list[i])):
        print(f'j = {j}')
        if plug_list[i+1][j] not in plug_list[:i + 1]:
            count += 1

print(count)