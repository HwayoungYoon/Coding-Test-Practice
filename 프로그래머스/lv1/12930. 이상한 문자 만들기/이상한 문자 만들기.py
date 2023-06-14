def solution(s):
    s = s.replace(' ','- ')
    answer = ''
    ss = s.split()
    for i in ss:
        for j in range(len(i)):
            if j%2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
    return answer.replace('-',' ')