def solution(before, after):
    bef = sorted(before)
    aft = sorted(after)
    if bef == aft:
        return 1
    else:
        return 0