def solution(array, height):
    # answer = 0
    # for a in array:
    #     if height < a:
    #         answer+=1
    answer = len([a for a in array if height<a])
    return answer