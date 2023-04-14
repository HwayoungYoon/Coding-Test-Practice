def solution(A, B):
    A = sorted(A)
    B = sorted(B)
    n = len(B)
    
    while len(A) > 0:
        a = A.pop()
        b = B.pop()
        if a < b:
            continue
        else:
            B.append(b)
    
    return n - len(B)