def solution(array, n):
    array = sorted(array)
    answer = []
    for i in array:
        answer += [abs(i-n)]
    return array[answer.index(min(answer))]