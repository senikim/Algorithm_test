# 인덱스+1
# [i-1:j-1], k-1

def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(sorted(array[c[0]-1:c[1]])[c[2]-1])
    return answer