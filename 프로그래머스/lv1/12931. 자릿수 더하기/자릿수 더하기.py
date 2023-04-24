def solution(n):
    st_n = str(n)
    answer = 0
    for i in range(len(st_n)):
        answer += int(st_n[i])
    return answer