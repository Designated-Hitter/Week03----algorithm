import sys
import heapq
input = sys.stdin.readline

N = int(input()) #N: 문제의 개수
problem_list = []

for _ in range(N):
    deadline, cup_ramen = map(int, input().split())
    problem_list.append([deadline, cup_ramen])https://www.msn.com/ko-kr/news/other/%EA%B9%80%EB%82%98%EC%98%81-%EA%B2%BD%EC%82%AC%EA%B0%80-%EC%9E%88%EC%97%88%EB%8B%A4-%EB%9F%B0%EB%8D%98%EC%97%90%EC%84%9C-%EC%95%A0%EA%B8%B0%EB%A5%BC-%EB%82%B3%EC%95%98%EC%96%B4%EC%9A%94/ar-AA1fRcaL?cvid=b527579aa43d406facf2f6ba51548187

# print(problem_list)

problem_list.sort(key= lambda x:x[0])
#힙을 활용하여 데드 라인 내에서 최대 컵라면 수를 구함
cup_ramen_heap = []
#-------------------------------이 부분이 잘 이해가 안감. openAI가 짜줌
for problem in problem_list:
    heapq.heappush(cup_ramen_heap, problem[1]) #problem[1]은 각 문제의 컵라면 개수
    if len(cup_ramen_heap) > problem[0]:  #problem[0]은 각 문제의 데드라인, 데드라인을 초과하는 문제는 힙에서 제거
        heapq.heappop(cup_ramen_heap)

print(sum(cup_ramen_heap))




#데드라인으로 오름차순 정렬, 컵라면 수로 내림차순 정렬 했더니 
#반례 [1, 1], [2, 1], [3, 10], [3, 10]을 해결하지 못함
# problem_list.sort(key=lambda x: (x[0], -x[1]))

# count = 1
# cup_ramen_get = 0
# for i in range(len(problem_list)):
#     if problem_list[i][0] >= count:
#         cup_ramen_get += problem_list[i][1]
#         count += 1

# print(cup_ramen_get)