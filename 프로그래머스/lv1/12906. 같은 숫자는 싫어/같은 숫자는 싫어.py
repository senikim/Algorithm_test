# 첫 풀이
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if answer[-1] == arr[i]:
            pass
        else:
            answer.append(arr[i])
    return answer
# 효율성테스트
# 테스트 1 〉	통과 (94.89ms, 27.8MB)
# 테스트 2 〉	통과 (170.93ms, 27.8MB)
# 테스트 3 〉	통과 (95.90ms, 27.9MB)
# 테스트 4 〉	통과 (89.83ms, 27.9MB)

# 다른 풀이 : USING STACK
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        answer.append(arr[i])
        if answer[-2] == arr[i]:
            answer.pop()
    return answer
# 효율성 테스트
# 테스트 1 〉	통과 (258.60ms, 28MB)
# 테스트 2 〉	통과 (151.24ms, 27.9MB)
# 테스트 3 〉	통과 (259.51ms, 27.9MB)
# 테스트 4 〉	통과 (138.16ms, 28MB)



# [TRIAL 1]
def solution(arr):
    answer = []
    for i in range(1, len(arr)+1):
        if arr[i-1] == arr[i]:
            arr.pop(i)
        else :
            pass
    answer.append(arr)
    return answer 
'''
# ERROR 1 : IndexError: list index out of range
range 안맞음
'''

# [TRIAL 2]
def solution(arr):
    answer = []
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            answer.append(arr[i-1])
        else :
            answer.append(arr[i])
    return answer  
'''
# Error 2. 중복되지 않는 값에 대한 조건 오류
- if절까지만 하면 연속적으로 중복되는 값에 대해 제거가 가능한데
- else에 포함되는 값은 추가가 안됨
'''

# [TRIAL 3]
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        answer.append(arr[i])
        if answer[-1] == arr[i]:
            answer.pop()
    return answer
'''
# Error.
- 항상 answer[-1] == arr[i]라서 결국 answer에 남아있는 값은 arr[0]값 뿐
- answer[-2]로 해보면 다를까 싶음
'''
