N = int(input())
a = []

for i in range(N):
    a.append(list(map(int, input().split())))
for b in sorted(a):
    print(b[0], b[1])