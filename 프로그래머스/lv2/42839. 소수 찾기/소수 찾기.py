from itertools import permutations

def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    case_pe = []
    case = []
    for i in range(1,len(numbers)+1):
        case_pe += permutations(numbers, i)
    for i in case_pe:
        n = int(''.join(i))
        if n not in case and n > 1:
            case += [n]
    answer = 0
    for i in case:
        if isprime(i) == True:
            answer += 1
    return answer