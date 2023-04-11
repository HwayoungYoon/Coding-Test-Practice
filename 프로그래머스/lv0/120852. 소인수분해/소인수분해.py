def solution(n):
    answer = []
    num = 2
    while num <= n:
        if n%num == 0:
            n /= num
            answer += [num]
        else:
            num += 1
    return sorted(list(set(answer)))