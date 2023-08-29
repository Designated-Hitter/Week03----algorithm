import sys
input = sys.stdin.readline

T = int(input()) #T: 테스트케이스의 개수
for _ in range(T):
    N = int(input()) #N: 지원자의 수
    recruit = []
    
    for _ in range(N):
        paper, interview = map(int, input().split())
        recruit.append([paper, interview])

    recruit.sort() #서류심사 기준으로 정렬
    min_interview_rank = recruit[0][1]  # 첫 번째 지원자의 면접 성적
    count = 1 #첫 지원자는 무조건 선발(서류 시험 1등 이니까)

    for i in range(1, N):
        if recruit[i][1] < min_interview_rank: #다음 지원자의 면접 순위가 기존의 min_rank보다 작으면(더 시험을 잘 봤으면) 합격
            count += 1
            min_interview_rank = recruit[i][1]
                
    print(count)

#메모리: 46764 KB
#시간: 4744 ms