from itertools import permutations
def solution(word):
    AEIOU = ['A','E','I','O','U']*5
    case = []
    dic = set()
    for i in range(1,6):
        case += permutations(AEIOU, i)
    for i in case:
        dic.add(''.join(i))
    dic = sorted(dic)
    return dic.index(word)+1