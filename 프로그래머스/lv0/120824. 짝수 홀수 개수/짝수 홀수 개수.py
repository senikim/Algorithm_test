def solution(num_list):
    answer = []
    odd = 0 #홀수
    even = 0 #짝수
    
    for n in range(len(num_list)):
        if num_list[n] % 2 == 0:
            even += 1
        else:
            odd += 1
    
    answer.append(even)
    answer.append(odd)
    
    return answer