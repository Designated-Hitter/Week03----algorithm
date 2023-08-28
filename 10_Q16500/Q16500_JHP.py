'''
    [효율성]
    - 메모리: 31256KB	
    - 시간: 44ms
'''
def sol(idx):
    # idx = 0
    global result

    # idx = 0, len(S) = 15 -> 'softwarecontest', A들로 S를 만들 수 있다면
    if idx == len(S): # 정답
        result = 1
        return
    
    if dp[idx]: # 이미 검사한 경우 dp[idx] != 0
        return
    
    # dp[0] = 1
    dp[idx] = 1 # 검사했으니 1로 만들어 줌
    
    # i = [0, 1]
    for i in range(len(A)): # A = ['software', 'contest']

        # S[0:] -> 모든 요소
        # S[8:] -> 리스트 A안에 있는 0번째 요소 통과 후 1번쨰 요소 확인
        # len(S[0:]) >= len(A[0]), 'software'
        if len(S[idx:]) >= len(A[i]): # S가 A[i] 보다 더 길 때만 비교 가능 

            # A[0] = 'software' -> j = [0, 1, 2, 3, 4, 5, 6, 7]
            for j in range(len(A[i])): # A에 포함된 단어 길이 
                # A = ['software', 'contest']

                # A[0][0] != S[0+0]: # S = 'softwarecontest'
                if A[i][j] != S[idx+j]: # A[i] 단어와 글자 하나하나 비교
                    break

            else:
                # A[i]와 S[:len(A[i])]
                sol(idx+len(A[i]))

    # 현재 S[index:]의 크기가 리스트 A에 남은 요소보다 크기가 작을 때,
    # 불가능 return (result 변화 없음, result == 0)
    return
    

S = input()

# 입력받은 문자들을 저장할 리스트
A = []

# 길이가 100이하인 문자열 S의 각 문자들을 저장할 리스트
dp = [0] * 101 # 메모제이션 
for _ in range(int(input())):
    A.append(input())

# 정답 여부 result -> A에 포함된 문자열들로 S를 만들수 있다면 1, 없으면 0
result = 0
sol(0)
print(result)