N = int(input())
M = int(input())
arr = list(map(int, input().split()))

# 모든 합의 경우를 고려하기 위해서 오름차순 정렬 (각각 left : 가장 작은 수, right : 가장 큰 수 에서 시작)
arr.sort()

left = count = sum_value = 0
right = N-1
    # [자기 자신 두 개의 재료를 모으면 안되고 다른 두 개의 재료를 모아야 하기 때문]

while left < right :
    # 현재 합 계산
    sum_value = arr[left] + arr[right]

    # 합 == M : count+=1, left += 1, right -= 1
    if sum_value == M:
        count += 1
        left += 1
        right -= 1
    # 합 < M
    elif sum_value < M :
        left += 1
    # 합 > M
    else :
        right -= 1
print(count)