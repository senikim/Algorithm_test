def solution(array):
    answer = 0
    # 정렬
    array = sorted(array)
    # 중간에 있는 -> 홀수 : length+1/2, 짝수 : length/2
    if len(array)%2 == 0:
        answer = array[(len(array)/2)-1]
    else:
        answer = array[int((len(array)+1)/2-1)]
        # answer = array[(len(array)+1)/2-1]
    return answer