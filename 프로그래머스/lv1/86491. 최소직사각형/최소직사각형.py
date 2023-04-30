def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i] = sorted(sizes[i], reverse=True)
    x = [i[0] for i in sizes]
    y = [i[1] for i in sizes]
    return max(x)*max(y)