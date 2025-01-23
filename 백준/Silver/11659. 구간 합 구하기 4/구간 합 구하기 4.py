import sys
input = sys.stdin.readline

N, no = map(int, input().split())
numbers = list(map(int, input().split()))
S = [0] # 합 배열
temp = 0 # S[i]=S[i-1]+A[i]

# 합 배열 만들기
for n in numbers:
    temp += n
    S.append(temp)
    
# 구간 합 구하기
for i in range(no):
    j, k = map(int, input().split())
    print(S[k]-S[j-1])