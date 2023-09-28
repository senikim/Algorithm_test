# 다시 풀어보기

VER1.
def solution(sizes):
    answer = 0
    w = []
    h = []
    for s in sizes:
        if s[0] > s[1]:
            w.append(s[0])
            h.append(s[1])
        else:
            w.append(s[1])
            h.append(s[0])
    answer = max(w)*max(h)
            
    return answer

VER2.
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


'''
TRIAL & EORROR

TRIAL4.
def solution(sizes):
    answer = 0
    width = []
    width2 = []
    width3 = []
    width4 = []
    height = []
    height2 = []
    height3 = []
    height4 = []
    
    for s in sizes:
        width.append(s[0])
        height.append(s[1])
    wmax = max(width)
    hmax = max(height)
    first = wmax*hmax
    
    for i in sizes:
        if i[0] == wmax:
            width2.append(i[1])
            height2.append(i[0])
        else:
            width2.append(i[0])
            height2.append(i[1])
    second = max(width2) * max(height2)
    
    for z in sizes:
        if z[1] == hmax:
            width3.append(z[1])
            height3.append(z[0])
        else:
            width3.append(z[0])
            height3.append(z[1])
    third = max(width3)*max(height3)
    
    for e in sizes:
        if e[0] == wmax:
            width4.append(e[1])
            height4.append(e[0])
        elif e[1] == hmax:
            width4.append(e[1])
            height4.append(e[0])
        else:
            width4.append(e[0])
            height4.append(e[1])
    fourth = max(width4) * max(height4)
    
    # return wmax, hmax, width2, hight2
    return min(first, second, third, fourth)
    
  # ERROR : 예외가 있었음 예시 4번
'''
