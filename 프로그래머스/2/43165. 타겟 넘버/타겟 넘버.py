answer = 0
def dfs_recursive(numbers, target, idx, value):
    global answer
    n = len(numbers)
    if n == idx and target == value:
        answer += 1
    elif n == idx:
        return
            # [return None]
    else:
        dfs_recursive(numbers, target, idx+1, value+numbers[idx])
        dfs_recursive(numbers, target, idx+1, value-numbers[idx])

def solution(numbers, target):
    dfs_recursive(numbers, target, 0, 0)
        # [idx, value = 0]
        # new
    return answer