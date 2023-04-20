def solution(score):
    mean = []
    answer = []
    for i in range(len(score)):
        mean += [sum(score[i])/2]
    sort_m = sorted(mean, reverse=True)
    for i in range(len(mean)):
        answer += [sort_m.index(mean[i])+1]
    return answer