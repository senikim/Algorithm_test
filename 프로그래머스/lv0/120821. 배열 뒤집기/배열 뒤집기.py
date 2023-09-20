def solution(num_list):
    answer = []
    for i in range(1, len(num_list)):
        answer.append(num_list[-i])
    answer.append(num_list[0])
    return answer


# 다른사람 풀이
def solution(num_list):
    answer = []
    return num_list[::-1]

def solution(num_list):
    answer = []
    while(num_list):
        answer.append(num_list.pop())
        # [num_list pop하면 뒤에서 부터 빠지니까 (선입선출) 그대로 answer에 append]
    return answer
