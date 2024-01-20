from collections import deque
import sys
from pprint import pprint

# n : 정점의 개수, m : 간선의 개수, v: 탐색 시작할 정점의 번호
n,m,v = map(int, input().split())

# 그래프 초기화
graph = [[False]*(n+1) for _ in range(n+1)]
    # [0번째 인덱스를 쓰지 않는 대신, 인덱스와 정점 간 계산의 편의성]
    # [6*6 그래프 : 노드 들 간의 관계를 보기 위해 만든 그래프]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    # [a, b가 연결되어 있다고 입력하면, 노드들의 관계를 나타낸 graph에서 연결이 가능하다는 표시로 True를 입력]
    # [graph에서 True인 애들로만 이동]

# 1-1) dfs 재귀
def dfs(node, visit):
    # [visit : 방문체크 행렬]
    # [node : 1, visit : [False]*(n+1)]
    visit[node] = True
    print(node, end=' ')
    for i in range(1, len(visit)):
        # [index 0 제외]
        # [visit의 행 수]
        if graph[node][i] and not visit[i]:
                # [graph에서 연결이 되어있음(True)+방문하지 않은 노드(not True)]
            dfs(i, visit)
# 2) bfs
def bfs(node, visit):
    queue = deque()
    queue.appendleft(node) # 후입후출(queue)
    while queue:
        next_node = queue.pop()
        if visit[next_node] : continue
            # [next_node가 방문된 노드면 무시]
        visit[next_node] = True
            # [next_node 방문처리]
        print(next_node, end=' ')
            # [방문 노드 출력]
        for i in range(1, len(visit)):
            if not graph[next_node][i]: continue
            queue.appendleft(i)
                # [queue에 후입]

dfs(v, [False]*(n+1))
print()
bfs(v, [False]*(n+1))