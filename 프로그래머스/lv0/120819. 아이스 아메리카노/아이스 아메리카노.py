def solution(money):
    answer = []
    n = money // 5500
    answer.append(n)
    answer.append(money-5500*n)
    return answer

# 몫만 출력 : //
# 나머지 출력 : %
# (몫, 나머지) 튜플 : divmod()
