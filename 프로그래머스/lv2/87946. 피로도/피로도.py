from itertools import permutations
def solution(k, dungeons):
    case = list(permutations(dungeons))
    dl = len(dungeons)
    answer = 0
    for li in case:
        ans = 0
        kk = k
        for i in li:
            if kk >= i[0]:
                kk -= i[1]
                ans += 1
            else:
                break
        if ans >= answer:
            answer = ans
    
    return answer