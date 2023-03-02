N = int(input())
a = []

for i in range(N):
    a.append(list(input().split()))
a.sort(key = lambda x:int(x[0]))

for b in a:
    print(b[0], b[1])