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



'''
# 하나씩
# 두개씩 : 17, 71 / 01,01,11 -> 01 = 1
# 세개씩 : 101 110 011 = 11
# 0이 맨 앞에 오면 맨 앞에 있는 0을 지우고 인식

    for n in range(len(num)):
        #return num[n]+num[n+1]
        m = 0
        while m <= len(n)-1:
            num[n]+num[m+1]
            m = m+1
        for a in range(len(all_list)):
        ','.join(all_list[a])
        
        
    # 소수 찾기
    for a in all_list:
        if a == 0 or a == 1:
            all_list.remove(a)
        else:
            pass
    
    # 소수찾기
    for a in all_list:
        boolean = True
        #["false" if a % k == 0 for k in range(2,a)]
        for k in range(2, int(math.sqrt(a)+1)):
            if a % k == 0:
                boolean = False
                break
        if boolean is True:
            print(a)
            answer += 1
        #all_list.remove(a)        
        #answer += 1


    for w in all_list:
        if w == 0 or w == 1:
            all_list.remove(w)
        else:
            pass

'''

# Trial 1. Error : 일반화가 됨
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
        
    # 소수 찾기
    for a in all_list:
        boolean = True
        if a == 0 or a == 1:
            all_list.remove(a)
            break
        else:
            pass
    for a in all_list:
        #["false" if a % k == 0 for k in range(2,a)]
        for k in range(2, a):
            if a % k == 0:
                boolean = False
                break
        if boolean is True:
            answer += 1
        #all_list.remove(a)        
        #answer += 1
return answer
