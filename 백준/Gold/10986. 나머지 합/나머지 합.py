N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*N
S[0] = A[0]
answer = 0
C = [0]*M  # 같은 나머지의 인덱스 카운트 - 나머지를 인덱스로 쓰고, 개수를 원소로 이용하기 때문에 M열 있어야 함.

# 배열 합 구하기
for i in range(1, N):
  S[i] = (S[i-1] + A[i])

# 배열 합 % M
for i in range(N):
  S[i] = S[i]%M
  if S[i] == 0 :
    answer += 1  # (구간 합%M) 자체가 0인 경우: 0번째부터 현재 위치까지의 합이 나누어 떨어진다는 거니까
  # 나머지 같은 원소 개수 구하기
  C[S[i]] += 1  # 인덱스: 나머지, 원소: 개수
  
# 조합 구하기: 나머지가 서로 같은 원소의 개수C2(조합)
for i in range(M):
  if C[i]>1:
    answer += (C[i]*(C[i]-1)) // 2  # 조합 - 나머지 같은 원소 중 2개 추출

print(answer)