def solution(dots):
    max_dots = max(dots)
    min_dots = min(dots)
    return (max_dots[0]-min_dots[0])*(max_dots[1]-min_dots[1])