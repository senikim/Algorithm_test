def solution(arr):
    answer=[]
    answer.append(arr[0])
    for a in range(1,len(arr)):
        if arr[a] == answer[-1]:
            pass
        else:
            answer.append(arr[a])            
    return answer