def solution(num_list):
    answer = []
    for i in range(1, len(num_list)):
        answer.append(num_list[-i])
    answer.append(num_list[0])
    return answer