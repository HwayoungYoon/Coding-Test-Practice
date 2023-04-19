def solution(numbers, direction):
    if direction == 'right':
        ans = [numbers[-1]]+numbers
        return ans[:-1]
    else:
        ans = numbers+[numbers[0]]
        return ans[1:]