def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse = True)
        # [각 원소(x)를 3번씩 반복해서 내림차순 정렬]
    numbers = str(int(''.join(numbers)))
    return numbers