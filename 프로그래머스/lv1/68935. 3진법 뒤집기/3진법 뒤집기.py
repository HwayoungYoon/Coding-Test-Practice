def solution(n):
    cross = ''
    while n > 0:
        n, mod = divmod(n, 3)
        cross += str(mod)
    return int(cross, 3)