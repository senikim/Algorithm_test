# Trial1. for문 이용하기
# 시간복잡도 : O(N)
N = input()
numbers = list(map(int, input().split()))
target = int(input())
n = 0
for i in numbers:
    if i == target:
        n+=1
print(n)

# Trial2. 리스트.count() 이용
# 시간복잡도 : O(N)
N = input()
numbers = list(map(int, input().split()))
target = int(input())
print(numbers.count(target))
