# [세로 방향 좌표, 가로 방향 좌표]

def solution(park, routes):
    x, y = 0, 0
    # 시작 위치 찾기
    for r in range(len(park)):
        for c in range(len(park[r])):
            if park[r][c] == 'S':
                x, y = r, c
    
    # 방향 좌표 설정
    loc = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
        # [이 문제에서는 x좌표 = row, y좌표 = col이기 때문에 좌표 반대로 설정]
        # ['S': 남쪽으로 이동 : col이 아래로 이동할 때마다 +1]
        # ['N': 북쪽으로 이동 : col이 위로 이동해야 됨 -> 왔던 길로 돌아가야지 위로 올라가게 됨]
    
    # routes 따라 이동
    for route in routes:
        dx, dy = loc[route.split()[0]]
            # [방향에 따른 좌표 설정]
        n = int(route.split()[1])
        xx, yy = x, y
            # [xx, yy : 이동한 위치들 반영]
        canmove = True  
            # [Flag 설정]
        
        # n번 이동
        for _ in range(n):
            nx = xx+dx  # x좌표 만큼 이동
            ny = yy+dy  # y좌표 만큼 이동
            
            # 이동 제약 반영 공원 안, 장애물
            if 0 <= nx <= len(park)-1 and 0 <= ny <= len(park[0])-1 and park[nx][ny] != 'X':
                canmove = True
                # 이동 제약 피했을 때 다음 이동 위치(xx,yy)를 이동한 위치(nx, ny)로 변경
                xx = nx
                yy = ny
                
            else :
                canmove = False
                break
                
        if canmove:
            x = nx
            y = ny
        
    
    return [x, y]
