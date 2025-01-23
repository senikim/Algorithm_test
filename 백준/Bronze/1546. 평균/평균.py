N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
print(sum(scores)*100/(M*N))