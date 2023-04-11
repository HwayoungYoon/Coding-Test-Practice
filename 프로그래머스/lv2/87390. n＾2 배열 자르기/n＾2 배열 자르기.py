def solution(n, left, right):
    x = []
    l = left//n
    r = right//n
    while l <= r+1:
        x += [l+1]*l + list(range(l+1,n+1))
        l += 1
    st = left%n
    en = st+right-left+1
    return x[st:en]