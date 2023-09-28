def solution(money):
    answer = []
    n = money // 5500
    answer.append(n)
    answer.append(money-5500*n)
    return answer