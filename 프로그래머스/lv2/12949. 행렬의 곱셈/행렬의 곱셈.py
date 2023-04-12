def inner(list1, list2):
    x = 0
    for i in range(len(list1)):
        x += list1[i]*list2[i]
    return x

def solution(arr1, arr2):
    ar2 = []
    for j in range(len(arr2[0])):
        ar2 += [[i[j] for i in arr2]]
    
    ans = [[0]*len(ar2) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(ar2)):
            ans[i][j] = inner(arr1[i],ar2[j])
    return ans