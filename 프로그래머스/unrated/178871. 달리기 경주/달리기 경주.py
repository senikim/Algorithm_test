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