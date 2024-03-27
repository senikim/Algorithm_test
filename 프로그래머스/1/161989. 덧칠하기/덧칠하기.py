def solution(n, m, section):
    answer = 1
        # [왜 answer = 1일까?]
    cur_start = section[0]
    for i in range(1, len(section)):
        if section[i]-cur_start >= m:
            answer+=1
            cur_start = section[i]
                # [section[0]부터 거리 비교했을 때 이미 m을 넘어서 answer에 1이 더해졌고,
                #  상황이 초기화 됨]
                # [이후 회차부터는 section[i]가 시작점이 된다]
    return answer