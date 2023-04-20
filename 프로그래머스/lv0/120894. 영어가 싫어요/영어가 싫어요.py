def solution(numbers):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        numbers = numbers.replace(eng[i], str(i))
    return int(numbers)