
# Trial 1.
def solution(a, b):
    answer = 0
    if a // 2 == 1 and b // 2 == 1 :
        answer += a^2 + b^2
    if a // 2 == 0 and b // 2 == 0 :
        answer += abs(a-b)
    else :
        answer += 2*(a+b)
    return answer
'''
# Error 1. 첫 번째 식의 결과값이 다르게 나옴.
- // 는 몫 연산자, % 가 나머지 연산자 -> % 써야 함.
- 거듭제곱 연산자는 **
'''

# Trial 2.
def solution(a, b):
    answer = 0
    if a % 2 == 1 and b % 2 == 1 :
        answer = a**2 + b**2
    if a % 2 == 0 and b % 2 == 0 :
        answer = abs(a-b)
    else:
        answer = 2*(a+b)
    return answer

'''
# Error 2. 계속 값이 틀림.
- if문이 두번 반복됨. -> if는 앞 조건이 충족되든 말든 진행하기 때문에 여러 조건을 한번에 만족시킬 수 없음.
- elif를 써야 함. -> elif는 앞 조건이 충족되지 않을 때 진행 됨.
'''

# 최종코드
def solution(a, b):
    answer = 0
    if a % 2 == 1 and b % 2 == 1 :
        answer = a**2 + b**2
    elif a % 2 == 0 and b % 2 == 0 :
        answer = abs(a-b)
    else:
        answer = 2*(a+b)
    return answer
