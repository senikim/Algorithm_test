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