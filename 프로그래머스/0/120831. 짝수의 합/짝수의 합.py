# 다른 사람 풀이 참고
def solution(n):
    return sum([i for i in range(2, n+1, 2)])


# 원래 내 처음 풀이
answer = 0
for i in range(1,n+1):
    if i%2==0:
        answer+=i
    else:
        pass    # else 안해도 됨
return answer
