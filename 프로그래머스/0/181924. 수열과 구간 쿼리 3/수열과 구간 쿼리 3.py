def solution(arr, queries):
    answer = []
    for q in queries:
        i, j = map(int, q)
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr