def solution(n, numlist):
    answer = [num for num in numlist if num%n==0]
    # for num in numlist:
    #     if num%n == 0:
    #         answer.append(num)
    return answer