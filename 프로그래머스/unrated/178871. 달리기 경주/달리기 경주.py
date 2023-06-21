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
def solution(players, callings):
    answer = []
    rank = []

    for i in range(len(players)):
      rank.append(i)
    print(rank)
    for g in range(len(callings)):
      #print(rank[players.index(callings[g])])
      rank[players.index(callings[g])] = rank[players.index(callings[g])]-1
      rank[players.index(callings[g])-1] = rank[players.index(callings[g])-1]+1
      print(rank)
        #rank[callings[g]] = rank[callings[g]]-1
#    print(rank)
#        if callings[i] == index[]
#    return answer

'''
[Trial]
- players의 인덱스를 따와서 '등수' 딕셔너리->리스트 만듦 (처음엔 딕셔너리로 하려다가 리스트로 바꿔서 해봄)
- callings 리스트 안에 있는 원소가 나올 때마다 '등수'배열에 있는 원소의 인덱스 -1 하고
  반대로 원래 그 자리에 있던 원소의 인덱스는 +1 하려고 함.

[Error]
- 원래 등수에 있던 원소를 찾게 하는 코드를 유기적으로 설계하지 못함.
- 'calling 리스트 안에 있는 원소 앞에 있던(리스트 기준 왼쪽에 위치한) 원소'를 '원래 등수에 있던 원소' 라고 설정했는데,
  그러면 반복되는 calling 값은 연산이 중복됨 (당연함.....)
'''

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
