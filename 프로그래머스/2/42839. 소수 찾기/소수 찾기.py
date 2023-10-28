from itertools import permutations
import math

def solution(numbers):
    answer = 0
    ex = []
    num = [*numbers]
    # [asterisk 이용해서 unpack]
    # [num = list(numbers)]
    pre_list = []
    all_list = []
    
    # all_list : 만들 수 있는 모든 숫자를 담은 리스트 생성
    for q in range(len(num)):
        pre_list.append(num[q])

    for i in range(2, len(num)+1):
        pre_list.append(list(permutations(num, i)))
    
    for p in range(len(pre_list)):
        for j in range(len(pre_list[p])):
            all_list.append(''.join(pre_list[p][j]))
    all_list = list(set(map(int, all_list)))
        # [문자형 -> 숫자형 (앞에 0먼저 오는 경우 처리)]
        # [set 중복제거]

    # 소수찾기
    all_list = [value for value in all_list if value != 0 and value != 1]

    for a in all_list:
        boolean = True
        for k in range(2, int(math.sqrt(a)+1)):
            if a % k == 0:
                boolean = False
                break
        if boolean is True:
            print(a)
            answer += 1

    return answer