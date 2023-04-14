def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == i:
                triangle[i][j] += triangle[i-1][j-1]
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])