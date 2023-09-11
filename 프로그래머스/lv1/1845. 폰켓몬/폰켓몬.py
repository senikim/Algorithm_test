# 다시 풀어보기

def solution(nums):
    unique = len(set(nums))
    if len(nums)/2 > unique:
        return unique
    else:
        return len(nums)/2