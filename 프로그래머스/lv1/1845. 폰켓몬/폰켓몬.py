# 가장 많은 종류의 폰켓몬 선택하는 방법
# 중복되지 않는 원소의 개수 

def solution(nums):
    answer = 0
    # 중복되지 않는 원소의 개수 < len(N/2)일 때 len(set(nums))
    if len(set(nums)) <= len(nums)/2:
        answer = len(set(nums))
    elif len(set(nums)) > len(nums)/2:
        answer = len(nums)/2
    # 중복되지 않는 원소의 개수 > len(N/2) 이면 len(N/2)출력
    return answer