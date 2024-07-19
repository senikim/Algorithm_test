# 기약분수
# 약분 = 최대공약수로 나누기
def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1*denom2+numer2*denom1
    denom = denom1*denom2
    number = 0  
    
    # 최대공약수 구하기
    start = max(numer, denom)
    for n in range(start, 0, -1):
        if numer%n == 0 and denom%n==0:
            number = n
            break;
    
    # 약분
    answer = [numer/number, denom/number]
    return answer