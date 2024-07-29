# code, date, maximum, remain

def solution(data, ext, val_ext, sort_by):
    # answer = [[]]
    answer = []
    col = {"code":0, "date":1, "maximum":2, "remain":3}
    for k,v in col.items():
        if k == ext:
            for d in data:
                if d[v] < val_ext:
                    answer.append(d)
    answer.sort(key= lambda x: x[col[sort_by]])
    return answer