def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                return False
            elif stack[-1] == '(':
                stack.pop()
            elif stack[-1] == ')':
                stack.append(i)
    if len(stack) == 0:
        return True
    else:
        return False

'''
# 첫 번째 풀이
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0 and i == ')':
            return False
        if i == '(':
            stack.append('(')
        if i == ')' and stack[-1] == '(':
            stack.pop()
    return False if len(stack) != 0 else True
'''