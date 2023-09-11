# 다시 풀어보기

# VER1.
def solution(nums):
    unique = len(set(nums))
    if len(nums)/2 > unique:
        return unique
    else:
        return len(nums)/2

# VER2.
def solution(nums):
    length = len(nums)/2
    unique = len(set(nums))
    return min(length, unique)

# VER3.
def solution(nums):
    min(len(nums)/2, len(set(nums))

'''
set() : 중복 제거 함수
'''
