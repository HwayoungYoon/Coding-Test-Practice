def solution(s):
    ss = s.lower()
    if ss.count('p') == ss.count('y'):
        return True
    else:
        return False