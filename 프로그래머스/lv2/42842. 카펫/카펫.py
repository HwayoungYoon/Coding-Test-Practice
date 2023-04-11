def solution(brown, yellow):
    ar = brown + yellow
    for i in range(1, int(yellow**0.5)+1):
        if yellow%i == 0:
            x = yellow/i+2
            y = i+2
            if ar == x*y:
                return[x, y]