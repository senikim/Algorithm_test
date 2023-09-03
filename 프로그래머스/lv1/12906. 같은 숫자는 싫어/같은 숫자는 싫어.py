def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if answer[-1] == arr[i]:
            pass
        else:
            answer.append(arr[i])
    return answer


# TRIAL & ERROR
# TRIAL1.
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
