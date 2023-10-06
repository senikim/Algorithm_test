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
