def solution(n):
    answer = 0
    # n//최대공약수
    # 최대공약수
    num = 0
    for i in range(min(6,n),1, -1):
        if 6%i == 0 and n%i==0:
            num = i
            break
    answer = n//num
    return answer
