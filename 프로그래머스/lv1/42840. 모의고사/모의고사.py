def solution(answers):
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0]*3
    for i in range(len(answers)):
        if answers[i] == m1[i%5]:
            correct[0] += 1
        if answers[i] == m2[i%8]:
            correct[1] += 1
        if answers[i] == m3[i%10]:
            correct[2] += 1
    max_n = max(correct)
    answer = []
    for i in range(3):
        if correct[i] == max_n:
            answer += [i+1]
    return answer