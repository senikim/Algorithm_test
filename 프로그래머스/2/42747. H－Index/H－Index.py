# 이해 못하겠음

def solution(citations):
    answer = 0
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            # [citations[i] : '인용된 횟수']
            # [l-i : 인용된 논문의 개수를 최댓값에서 부터 하나씩 줄여나감]
            return l-i
    return 0