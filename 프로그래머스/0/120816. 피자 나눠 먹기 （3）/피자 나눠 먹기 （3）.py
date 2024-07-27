def solution(slice, n):
    if slice >= n :
        return 1
    else:
        return (n+slice-1)//slice