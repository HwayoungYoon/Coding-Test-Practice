def solution(spell, dic):
    answer = 2
    spell = set(spell)
    for i in dic:
        if len(list(spell - set(i))) == 0:
            answer = 1
    return answer