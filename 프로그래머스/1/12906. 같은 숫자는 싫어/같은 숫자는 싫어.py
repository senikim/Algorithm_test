def solution(arr):
    answer = []
    answer.append(arr[0])
    for a in arr[1:]:
        if answer[-1] != a:
            answer.append(a)
    return answer