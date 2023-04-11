def solution(n):
    answer = []
    num = 2
    while num <= n:
        if n%num == 0:
            n /= num
            if num not in answer:
                answer += [num]
        else:
            num += 1
    return answer