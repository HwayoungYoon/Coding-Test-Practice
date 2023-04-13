from collections import deque
def solution(people, limit):
    people = deque(sorted(people))
    answer = 0
    while len(people) > 0:
        if len(people) == 1:
            answer += 1
            break
        elif people[0]+people[-1] <= limit and len(people)>1:
            people.pop()
            people.popleft()
            answer += 1
        elif people[0]+people[-1] > limit and len(people)>1:
            people.pop()
            answer += 1
    return answer