import re
def solution(my_string):
    answer = re.findall(r'\d', my_string)
    return sorted(list(map(int, answer)))