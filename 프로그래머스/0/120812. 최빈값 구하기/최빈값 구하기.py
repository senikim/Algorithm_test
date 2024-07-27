from collections import Counter
def solution(array):
    answer = 0
    count = Counter(array)
    mode = [k for k, v in count.items() if v == max(count.values())]
    if len(mode) > 1:
        return -1
    else:
        return mode[0]