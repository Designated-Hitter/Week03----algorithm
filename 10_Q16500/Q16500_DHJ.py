import sys
input = sys.stdin.readline
S = str(input().rstrip())
S_list = list(S)

N = int(input())
dp = [0] * (len(S_list) + 1)
dp[0] = 1

words = []
for _ in range(N):
    word = str(input().rstrip())
    words.append(word)

for i in range(len(S_list) + 1):
    for word in words:
        word_len = len(word)
        #i가 비교하고자 하는 단어보다 길거나 같고, i 직전까지의 단어가 이미 비교가 되었으며(=dp == 1이며), slice 한 부분이 word와 똑같다면
        if i >= word_len and dp[i - word_len] == 1 and S_list[i - word_len:i] == list(word):
            dp[i] = 1
#dp의 마지막 배열의 값이 1이라면
if dp[len(S_list)]:
    print(1)
else:
    print(0)