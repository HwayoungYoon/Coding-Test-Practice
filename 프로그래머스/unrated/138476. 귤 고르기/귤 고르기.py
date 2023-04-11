import collections
def solution(k, tangerine):
    answer = 0
    n = 0
    count = sorted(collections.Counter(tangerine).values(), reverse=True)
    while k > 0:
        k = k-count[n]
        answer += 1
        n += 1
    return answer