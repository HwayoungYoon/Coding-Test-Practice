def solution(emergency):
    sort_em = sorted(emergency, reverse=True)
    answer = []
    for i in range(len(emergency)):
        answer += [sort_em.index(emergency[i])+1]
    return answer