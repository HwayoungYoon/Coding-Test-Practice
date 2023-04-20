def solution(n):
    x = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    xx = range(4, n+1)
    return len(list(set(xx)-set(x)))