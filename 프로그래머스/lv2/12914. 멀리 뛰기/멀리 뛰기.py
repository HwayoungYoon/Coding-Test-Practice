def solution(n):
    a = 1
    b = 2
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(n-2):
            a, b = b, a+b
        return b % 1234567