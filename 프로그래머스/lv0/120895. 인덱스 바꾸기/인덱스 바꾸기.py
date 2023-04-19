def solution(my_string, num1, num2):
    my_s = list(my_string)
    my_s[num1] = my_string[num2]
    my_s[num2] = my_string[num1]
    return ''.join(my_s)