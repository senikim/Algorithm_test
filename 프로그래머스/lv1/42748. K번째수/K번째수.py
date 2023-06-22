def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        
        cut = array[i-1:j]
         # [이 문제에서는 인덱스 1부터 시작]
         # [슬라이싱할 때, i:j로하면 j-1번째 수까지만 출력됨.]
        cut.sort()
        answer.append(cut[k-1])
    return answer



# [Trial 1]
def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        
        cut = array[i-1:j]
         # [이 문제에서는 인덱스 1부터 시작]
         # [슬라이싱할 때, i:j로하면 j-1번째 수까지만 출력됨.]
        answer.append(cut[k])
    return answer

'''
# [Error] 답이 다름
# [Solution] 정렬을 안함
'''

# 다른 사람 풀이 참고 - 한줄 코드
def solution(array, commands):
    return list(map(lambda x: sorted(x[0]-1:x[1])[x[2]-1], commands))

