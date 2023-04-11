def solution(s):
    ss = s.split()
    answer = []
    for i in ss:
        if i != 'Z':
            answer.append(int(i))
        else:
            answer.pop()
    return sum(answer)

'''
# 첫 번째 풀이
import re
def solution(s):
    ss = s.split()
    for i in range(1, len(ss)):
        if ss[i] == "Z":
            ss[i] = 1
            ss[i-1] = -1
    ss = list(map(int, ss))
    return sum(ss)
'''