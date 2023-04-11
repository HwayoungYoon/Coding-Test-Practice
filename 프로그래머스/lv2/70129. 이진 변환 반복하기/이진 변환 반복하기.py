def solution(s):
    count, num = 0, 0
    while s != '1':
        count += s.count('0')
        s_len = len(s)-s.count('0')
        s = bin(s_len)[2:]
        num += 1
    return [num, count]