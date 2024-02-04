# 거쳤던 칸을 다시 거쳐도 됨 -> 중복처리 필요X
# 임의의 위치에서 시작 -> 파라미터로 지정
# 모든 칸을 방문해야 함 -> dfs

board = [list(map(int, input().split())) for _ in range(5)]
    # [5*5 숫자판 만들기]
numbers = set()
    # [서로 다른 여섯자리 수들의 집합]

def dfs(x, y, depth, num):
    # [x, y : 시작점, depth: 몇 번째 실행 중인지, num : 결과]
    if depth == 6:
        numbers.add(num)
        return
    # 제약조건 어겼을 때
    if x<0 or x>=5 or y<0 or y>=5 :
        return
    dfs(x+1, y, depth+1, num*10+board[x][y])
        # [board[x][y] : 현재 방문한 위치에 있는 수 (number 뒤에 추가되는 숫자)]
    dfs(x-1, y, depth+1, num*10+board[x][y])
    dfs(x, y+1, depth+1, num*10+board[x][y])
    dfs(x, y-1, depth+1, num*10+board[x][y])
    
numbers.clear()
for x in range(5):
    for y in range(5):
        dfs(x,y,0,0)
print(len(numbers))