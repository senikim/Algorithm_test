def solution(survey, choices):
    answer = ''
    dic = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for i in range(len(survey)):
        l = survey[i][0]
        r = survey[i][1]
        
        if choices[i] == 4:
            pass
        elif choices[i] == 1:
            dic[l] += 3
        elif choices[i] == 2:
            dic[l] += 2
        elif choices[i] == 3:
            dic[l] += 1
        elif choices[i] == 5:
            dic[r] += 1
        elif choices[i] == 6:
            dic[r] += 2
        elif choices[i] == 7:
            dic[r] += 3
    
    answer += "R" if dic["R"] >= dic["T"] else "T"
    answer += "C" if dic["C"] >= dic["F"] else "F"
    answer += "J" if dic["J"] >= dic["M"] else "M"
    answer += "A" if dic["A"] >= dic["N"] else "N"
    
    return answer