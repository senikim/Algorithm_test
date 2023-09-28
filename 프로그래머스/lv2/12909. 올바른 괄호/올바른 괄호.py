# 다시풀어보기
# 스택 :: 스택이 비어있는지, 비어있지 않은지로 True/False 출력하는 방법

def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else: # [i가 ")"인 경우일 때]
            if stack:
                # [stack이 비어있지 않다면]
                stack.pop()
                    # [이미 stack에 들어있는 "("와 짝이 되는 ")"이라는 뜻, stack을 소거시킴(약간 상쇄되는 느낌으로)]
            else:
                #[stack이 비어있다면]
                return False
                    #[stack이 비어있지 않으면 짝이 맞지 않는다는 거니까 잘못된 괄호]
    if stack:
        # [전체적으로 stack이 비어있지 않다면]
        return False
    return True
            