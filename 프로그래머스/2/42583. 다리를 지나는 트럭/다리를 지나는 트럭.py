# 일차선 다리를 정해진 순서대로 건널 때
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지
# 다리에 있는 트럭들의 수 <= bridge_length
# 다리에 있는 트럭들의 무게 합 <= weight
# 다리를 지난 트럭, 다리 위에 있는 트럭, 대기 트럭

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0 
    bridge = deque([0]*bridge_length)
        # [brigde 자체를 해시로 만듦]
    truck_weights = deque(truck_weights)
    
    cur_weight = 0
        # [현재 다리 위에 있는 트럭들의 무게]
    while truck_weights:
            # [아직 다리를 안건넌 트럭이 있으면 반복]
        answer += 1
        cur_weight -= bridge.popleft()
            # [1초마다 가장 먼저 들어온 차량이 다리를 다 지나가기 때문에]
            # [현재 다리 위에 있는 차량들의 무게 합에서 빼준다.]
        if cur_weight + truck_weights[0] <= weight:
            cur_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
                # [무게 초과하면 트럭 안옮김]
    answer += bridge_length
        # [다리 위에 있는 차만큼 다 움직여야 하기 때문에]
    return answer    