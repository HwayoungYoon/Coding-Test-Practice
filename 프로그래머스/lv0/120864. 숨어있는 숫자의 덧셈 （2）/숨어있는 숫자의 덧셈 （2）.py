import re
def solution(my_string):
    str_remove = re.findall(r'\d+', my_string)
    return sum(list(map(int, str_remove)))