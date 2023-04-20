def solution(my_str, n):
    answer = []
    num = 0
    while num < len(my_str):
        answer += [my_str[num:num+n]]
        num = num+n
    return answer