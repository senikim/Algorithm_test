def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            # [이러면 동명이인 걸러짐, sort된 상태에서 비교하니까]
            return participant[i]
    return participant[-1]
    # [sort한 두 배열이 위에서 completion의 길이 만큼 loop돌았는데도 발견못했으니까 결국 participant의 맨 마지막 원소가 답이 됨]

'''
# TRIAL & ERROR

# 완주하지 못한 단 한명의 선수 출력 
# 동명이인 처리
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for c in range(len(completion)):
        if participant[c] != completion[c]:
            answer = participant[c]
            break [#for문 밖으로]
	    
        # 예외처리 : for문 다 돌았는데도 배열 간 다른 원소 없으면 
        # participant의 맨 마지막 원소 출력
        answer = participant[-1]
    return answer

# Error
어디가 틀렸을까
'''

# 다른사람 풀이
import collections

def solution(participant, completion):
	answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
    
'''
나는 차집합 한다고 list[set(part) - set(comp)] 했었는데 이러면 중복되는게 다 사라져서 잘못된 풀이였음
'''
