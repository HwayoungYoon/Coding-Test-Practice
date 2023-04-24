def solution(x):
    st_x = str(x)
    sum_x = 0
    for i in range(len(st_x)):
        sum_x += int(st_x[i])
    if x%sum_x == 0:
        return True
    else:
        return False