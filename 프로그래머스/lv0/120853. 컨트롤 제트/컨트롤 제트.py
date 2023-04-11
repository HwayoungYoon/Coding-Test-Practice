import re
def solution(s):
    ss = s.split()
    for i in range(1, len(ss)):
        if ss[i] == "Z":
            ss[i] = 1
            ss[i-1] = -1
    ss = list(map(int, ss))
    return sum(ss)