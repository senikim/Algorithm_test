# 해당 프로세스가 몇 번째로 실행되는지
# priorities 클 수록 우선순위 높음

def solution(priorities, location):
    answer = 0
    que = [(e,v) for e,v in enumerate(priorities)]
    while True:
        cur = que.pop(0)
            # [priorities의 첫 원소부터 순서대로 시작하니까 cur에 담아서 확인함]
        if any(cur[1] < q[1] for q in que):
            # [cur의 value부분이 que의 value부분보다 작은게 하나라도 있으면 다음 순서로 넘어가야 함]
            que.append(cur)
                # [우선순위가 낮은 원소라는 거니까 다시 que에 넣음]
        else:
            answer += 1
                # [우선순위가 가장 높은 원소면 프로세스 하나 끝내는거니까 answer += 1]
            if cur[0] == location:
                # [cur[0]는 index == 위치]
                # [계속 answer더하다가 cur[0] == location인 부분에서 answer 출력]
                return answer