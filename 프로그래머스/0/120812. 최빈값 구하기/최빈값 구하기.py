# Trial1.
def solution(array):
    answer = 0
    # 원소 set
    answer_dict = {}
    for i in set(array):
        answer_dict[i] = array.count(i)
    # value 값 중 가장 큰 key 출력
    if len([k for k,v in answer_dict.items() if max(answer_dict.values())==v]) < 2:
        return max(answer_dict, key=answer_dict.get)
    else :
        return -1

# Trial2. 개선코드
from collections import Counter
def solution(array):
    answer = 0
    count = Counter(array)
    mode = [k for k, v in count.items() if v == max(count.values())]
    if len(mode) > 1:
        return -1
    else:
        return mode[0]
