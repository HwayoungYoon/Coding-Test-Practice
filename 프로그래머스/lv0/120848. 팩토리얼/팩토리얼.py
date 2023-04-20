def solution(n):
    ans = n
    num = 1
    while num <= 11:
        ans = ans//num
        num += 1
        if ans == 0:
            break
    return num-2