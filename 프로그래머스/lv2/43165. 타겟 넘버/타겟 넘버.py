from itertools import combinations
def solution(numbers, target):
    n = (sum(numbers)-target)/2
    answer = 0
    num = [x for x in numbers if x <= n]
    x = [num]
    for i in range(1, len(num)):
        x += combinations(num,i)
    for i in x:
        if sum(i) == n:
            answer += 1
    return answer

'''
numbers 합에서 target 뺀 값을 2로 나눈 값이 n이라고 하면
numbers 중 일부를 더해 n으로 만들 수 있는 경우의 수가 답
'''