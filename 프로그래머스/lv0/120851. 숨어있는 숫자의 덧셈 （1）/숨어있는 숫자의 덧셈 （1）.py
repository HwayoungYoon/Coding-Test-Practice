import re
def solution(my_string):
    ans = re.findall(r'\d', my_string)
    return sum(list(map(int, ans)))