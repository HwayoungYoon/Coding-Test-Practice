def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        ar = arr[i]
        if answer[-1] != ar:
            answer.append(ar)
    return answer