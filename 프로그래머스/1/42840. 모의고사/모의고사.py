def solution(answers):
    answer = []
    f = []
    s = []
    t = []
    dic = {}
    
    while len(f) <= len(answers):
        for i in range(1,6):
            if len(f) <= len(answers):
                f.append(i)
            if len(f) == len(answers):
                break
    
    while len(s) <= len(answers):
        for q in (2,1,2,3,2,4,2,5):
            if len(s) <= len(answers):
                s.append(q)
            if len(s) == len(answers):
                break
    
    while len(t) <= len(answers):
        for w in (3,3,1,1,2,2,4,4,5,5):
            if len(t) <= len(answers):
                t.append(w)
            if len(t) == len(answers):
                break
    
    for a in range(len(answers)):
        if answers[a] == f[a]:
            dic[1] = dic.get(1, 0)+1
        if answers[a] == s[a]:
            dic[2] = dic.get(2, 0)+1
        if answers[a] == t[a]:
            dic[3] = dic.get(3, 0)+1

    return sorted([k for k, v in dic.items() if v == max(dic.values())])