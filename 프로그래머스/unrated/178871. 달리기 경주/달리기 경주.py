# [최종 답안]
def solution(players, callings):
    
    player = {player : rank for rank, player in enumerate(players)}
    rank = {rank : player for rank, player in enumerate(players)}
    
    for call in callings:
        cur_rank = player[call]
        front_rank = cur_rank-1
        
        cur_player = call
        front_player = rank[front_rank]
        
        player[cur_player], player[front_player] = front_rank, cur_rank
         # [player는 결국, front_rank, cur_rank를 구하기 위한 거였음.]
        rank[cur_rank], rank[front_rank] = front_player, cur_player
        
    return list(rank.values())


# [Trial 1]



# [Trial 2]
def solution(players, callings):
    answer = []
    
    player = {player : rank for rank, player in enumerate(players)}
    rank = {rank : player for rank, player in enumerate(players)}
    
    for call in callings:
        cur_rank = player[call]
        front_rank = cur_rank-1
        
        cur_player = call
        front_player = rank[front_rank]
        
        player[cur_player], player[front_player] = front_rank, cur_rank
         # [player는 결국, front_rank, cur_rank를 구하기 위한 거였음.]
        rank[cur_rank], rank[front_rank] = front_player, cur_player
        
        answer=list(rank.values())
        
    return answer
'''
# Error : 시간초과
- 처음엔 몰랐는데 보니까 for문 안에 answer=list(rank.values())를 넣어서 answer안에 값을 일일이 집어넣는 과정에서 시간초과가 일어났음.
- 바로 [최종 답안]처럼 냅다 list(rank.values())를 print함.
'''
