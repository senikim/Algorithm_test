n = int(input())
s, g, p, d = list(map(int, input().split()))
rank = list(map(str, input().strip()))
prev = [0]

for i in range(n):
    bplus = s - prev[-1] - 1
    splus = g - prev[-1] - 1
    gplus = p - prev[-1] - 1
    pplus = d - prev[-1] - 1
    dplus = d    # [한달 최대 과금액 : 다이아몬드 기준액]
    
    if rank[i] == 'B':
        prev.append(bplus)
    elif rank[i] == 'S':
        prev.append(splus)
    elif rank[i] == 'G':
        prev.append(gplus)
    elif rank[i] == 'P':
        prev.append(pplus)
    elif rank[i] == 'D':
        prev.append(dplus)
        
print(sum(prev))