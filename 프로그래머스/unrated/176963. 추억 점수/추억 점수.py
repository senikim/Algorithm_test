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


# TRIAL 1
def solution(name, yearning, photo):
    answer = []
    score = {}
    final_score = 0
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    for g in photo:
      for n in range(len(g)):
        final_score += score[g[n]]
      answer.append(final_score)
    return answer
    
'''
# ERROR : 'brin'이 없음
# yearning에 없는 이름은 pass하고 점수를 더해야 함
'''

# TRIAL 2
def solution(name, yearning, photo):
    answer = []
    score = {}
    final_score = 0
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    for g in photo:
        for n in range(len(g)):
            if g[n] in name:
                final_score += score[g[n]]
            else:
                pass
        answer.append(final_score)
    return answer
    
'''
# ERROR : 결과값이 다름
# for g in photo : 때문에 photo[0]까지는 괜찮은데 다음 원소부터는 이전 원소값이 누적돼서 더해지는 오류 발생
# for g in photo 시작 후에 final_score 초기화 해주기 -> for g in photo : final_score = 0
'''
