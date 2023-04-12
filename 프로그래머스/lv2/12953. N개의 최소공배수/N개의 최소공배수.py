import math
def solution(arr):
    gcd = arr[0]
    lcm = arr[0]
    for i in range(1, len(arr)):
        gcd = math.gcd(lcm, arr[i])
        lcm = lcm*arr[i]//gcd
    return lcm