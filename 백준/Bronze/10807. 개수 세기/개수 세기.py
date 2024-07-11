N = input()
numbers = list(map(int, input().split()))
target = int(input())
n = 0
for i in numbers:
    if i == target:
        n+=1
print(n)