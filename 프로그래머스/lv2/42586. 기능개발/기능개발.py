import math
def solution(progresses, speeds):
    answer = [1]
    term = []
    for i in range(len(progresses)):
        term += [math.ceil((100-progresses[i])/speeds[i])]
    print(term)
    for i in range(1,len(term)):
        if term[i-1] >= term[i]:
            term[i] = term[i-1]
            answer[-1] += 1
        else:
            answer += [1]
    return answer