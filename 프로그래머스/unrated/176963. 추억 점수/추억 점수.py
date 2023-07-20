def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    for g in photo:
        final_score = 0
        for n in range(len(g)):
            if g[n] in name:
                final_score += score[g[n]]
            else:
                pass
        answer.append(final_score)
    return answer