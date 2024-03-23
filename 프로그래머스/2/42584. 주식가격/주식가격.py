# 입력값 : 초 단위로 기록된 주식가격이 담긴 배열
# 출력 : 가격이 떨어지지 않은 기간이 몇 초인지
from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        price = queue.popleft()
        time = 0
        for q in queue:
            time+=1
            if price > q:
                break
        answer.append(time)
    
    return answer