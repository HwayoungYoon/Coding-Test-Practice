def solution(numbers, k):
    answer = numbers*k
    return answer[(k-1)*2]