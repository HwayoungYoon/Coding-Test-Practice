def solution(n):
    x = []
    for i in range(1,300):
        if i%3 != 0:
            if '3' not in str(i):
                x += [i]
    return x[n-1]