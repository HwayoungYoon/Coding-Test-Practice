def solution(numbers):
    numbers.sort(reverse=True)
    return max(numbers)*numbers[1]