def solution(arr):
    del arr[arr.index(min(arr))]
    if arr == []:
        return [-1]
    else:
        return arr