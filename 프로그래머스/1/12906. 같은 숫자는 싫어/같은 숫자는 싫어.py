def solution(arr):
    answer = []
    answer.append(arr[0])    # 개선점 : 그냥 처음부터 answer=[arr[0]]
    for a in arr[1:]:
        if answer[-1] != a:
            answer.append(a)
    return answer


# 다른 풀이
def solution(arr):
    # arr이 비어있으면 빈 리스트 반환 / if not : ~하지 않으면 (arr이 채워져있지 않으면)
    if not arr:
        return []
        
    answer = []    #stack
    for num in arr:
        if not answer or answer[-1] != num:    # answer가 비어있거나(맨 첫 원소) answer의 마지막 원소가 num이랑 다르면 append
            answer.append(num)
    return answer
