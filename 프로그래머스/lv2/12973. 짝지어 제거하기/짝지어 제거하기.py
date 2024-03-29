def solution(s):
    s = list(s)
    stack = [s[0]]
    for i in range(1,len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif len(stack) > 0 and stack[-1] == s[i]:
            stack.pop()
        elif len(stack) > 0 and stack[-1] != s[i]:
            stack.append(s[i])
    if len(stack) == 0:
        return 1
    else:
        return 0