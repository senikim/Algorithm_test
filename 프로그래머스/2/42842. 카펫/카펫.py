# brown : 갈색 격자 수 >= 8, 테두리 한줄
# yellow : 노란색 격자 수 >= 1
# answer = [카펫의 가로, 세로 크기]

def solution(brown, yellow):
    answer = []
    num = []
    pre_answer = []
    
    # 두 수를 곱해서 yellow가 되는 경우 구하기
    for i in range(1, yellow+1):
        if yellow % i == 0 and i >= yellow/i:
            num.append([i, yellow/i])
            # [가로 >= 세로]
    
    for n in range(len(num)):
        if num[n][0]*2 + num[n][1]*2 == int(brown) - 4:
            pre_answer.append(num[n])
    
    answer.append(pre_answer[0][0]+2)
    answer.append(pre_answer[0][1]+2)
    
    return answer