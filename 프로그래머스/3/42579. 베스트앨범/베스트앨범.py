# 장르별 재생된 곡 수 많은 순
# 장르 내 가장 많이 재생된 노래 수
# 재생 수 같으면 고유 번호 낮은 노래 수록

def solution(genres, plays):
    answer = []
    music = []
    dic = {}
    #pre = []
    
    for m in enumerate(zip(plays, genres)):
        music.append(m)
    
    for g in range(len(genres)):
        if genres[g] == music[g][1][1]:
            dic[genres[g]] = dic.get(genres[g],0) + music[g][1][0]
        else:
            pass
        # [dic : genre별 재생횟수의 누적 합]
    dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
        # [value(재생횟수)가 큰 순서대로 내림차순 정렬]
    music = sorted(music, key = lambda x: x[1][0], reverse = True)
        # [music 안에서 plays 많은 순서대로 내림차순 정렬]

    for i in range(len(dic)):
        q = 0
        for u in range(len(music)):
            if music[u][1][1] == dic[i][0]:
                answer.append(music[u][0])
                q += 1
            else:
                pass
            if q == 2:
                break

    return answer

'''
    for i in range(len(dic)):
        for u in range(0, len(music)-1):
            if dic[i][0] == music[u][1][1]:
                answer.append(music[u][0])
                if music[u][1][0] <= music[u+1][1][0]:
                    answer.pop()
                    answer.append(music[u+1][0])
                else:
                    pass
            else:
                pass
'''

'''
def asterisk(arg):
    print(*arg)
music = asterisk(music)
'''