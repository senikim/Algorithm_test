# 인덱스+1
# [i-1:j-1], k-1

def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(sorted(array[c[0]-1:c[1]])[c[2]-1])
    return answer


# 이전 최종코드
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


# 한줄코딩
def solution(array, commands):
 return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
