def solution(n):
    answer = 0
    for i in range(n//2):
        answer += 2*(i+1)
    return answer