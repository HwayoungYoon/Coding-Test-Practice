def solution(x, n):
    answer = []
    for i in range(n):
        answer += [x*(1+i)]
    return answer