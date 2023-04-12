from itertools import combinations
def solution(numbers, target):
    
    n = (sum(numbers)-target)/2
    num = [x for x in numbers if x <= n]
    x = [num]
    for i in range(1, len(num)):
        x += combinations(num,i)
    
    answer = 0
    for i in x:
        if sum(i) == n:
            answer += 1
    
    return answer