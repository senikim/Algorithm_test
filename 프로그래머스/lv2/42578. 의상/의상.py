def solution(clothes):
    answer = 0
    hash_map = {}
    # 옷 종류별로 분류하기
    for clo, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
            # [type에 맞는 value가 있으면 가져오고, 없으면 0]
            # [맨처음엔 다 없을테니까 1더해서 시작, 반복할 수록 같은 type에 해당하는 옷이 있으면 value값이 +1 씩 증가 => 즉, value = 옷의 가짓수]

    # 전체 경우의 수
    answer = 1
    for type in hash_map:
        answer *= (hash_map[type] + 1)
            # [마지막 +1 : 안입는 경우까지 포함]
        
    return answer - 1 #아무것도 입지 않는 경우 제외


# Trial 1. 어떤 건 맞고 어떤 건 틀림 - 근데 일단 풀이 방법은 맞았음

# 종류별로 나누고 그 개수에 +1(아예 안걸치는거), 종류별로 곱하고 -1(모든 종류가 0일 경우 제외)
# 만약 종류가 하나밖에 없으면 개수 그대로 (최소 하나는 꼭 입어야 하니까)

from collections import Counter
def solution(clothes):
    answer = 0
    category = []
    key = []
    value = []

    for c in clothes:
        category.append(c[1])
    count = Counter(category)
    for k, v in count.items():
        key.append(k)
        value.append(v)

    if len(key) > 1:
        for v in range(len(value)):
            value[v] += 1
        return [value[i] * value[i+1] -1 for i in range(len(value)-1)][0]
    return sum(value)
