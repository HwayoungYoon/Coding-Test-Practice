from queue import Queue
def solution(n):
    a = list(range(n))
    S = set()
    answer = 1
    for i in a:
        num = i*(i+1)//2
        S.add(num)
        if num - n in S:
            answer += 1
    return answer