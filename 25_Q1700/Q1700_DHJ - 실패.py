import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #N: 멀티탭 구멍의 개수, K: 전기용품의 총 사용횟수

elec_list = list(map(int, input().split()))
print(elec_list)
#[2,3,2,3,1,2,7]
# plug_list = [elec_list[i:i + N] for i in range(0, len(elec_list), N)]
no_dup = [elec_list[0]]
for i in range(1, len(elec_list)): #연속된 전자기기가 같은 경우 제거
    if elec_list[i - 1] == elec_list[i]:
        continue
    else:
        no_dup.append(elec_list[i])
print(no_dup)

plug_list = []
multitap = set() #멀티탭을 set으로 선언해 멀티탭 안에 [1,2,1] 같은 똑같은 기기가 다른 곳에 꼽히는 경우를 삭제함
for i in range(len(no_dup)):
    multitap.add(no_dup[i])
    if len(multitap) == N or i == len(no_dup) - 1:
        multitap_done = list(multitap) #중복을 제거한 멀티탭의 경우를 계산하기 쉽게 list로 변환

        plug_list.append(multitap_done)
        multitap.clear()
print(plug_list)
#[[2,3],[2,3],[1,2],[7]]
count = 0

for i in range(1, len(plug_list)):
    for j in range(len(plug_list[i])):
        if plug_list[i][j] not in plug_list[i - 1]:
            count += 1

print(count)