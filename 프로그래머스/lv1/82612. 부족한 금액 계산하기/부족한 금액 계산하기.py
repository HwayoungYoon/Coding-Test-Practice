def solution(price, money, count):
    cost = price*count*(count+1)/2 - money
    if cost > 0:
        return cost
    else:
        return 0