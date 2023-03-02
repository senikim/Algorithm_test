N = int(input())
a = []

for i in range(N):
    a.append(list(map(int, input().split())))
a.sort(key = lambda x: (x[1],x[0]))

for b in a:
    print(b[0], b[1])