from collections import Counter
def solution(array):
    com = Counter(array).most_common()
    while len(com) > 1:
        if com[0][1] == com[1][1]:
            return -1
        else:
            return com[0][0]
    return com[0][0]