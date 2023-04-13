from collections import deque
def solution(priorities, location):
    pr = deque(priorities)
    answer = 0
    while True:
        if pr[0] == max(pr):
            answer += 1
            if location == 0:
                break
            else:
                pr.popleft()     
                location -= 1
        else:
            if location == 0:
                x = pr.popleft()
                pr.append(x)
                location = len(pr)-1
            else:
                x = pr.popleft()
                pr.append(x)
                location -= 1
    return answer