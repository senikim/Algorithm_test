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


# 다른사람 풀이
import collections

def solution(participant, completion):
	answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
    
'''
나는 차집합 한다고 list[set(part) - set(comp)] 했었는데 이러면 중복되는게 다 사라져서 잘못된 풀이였음
'''
