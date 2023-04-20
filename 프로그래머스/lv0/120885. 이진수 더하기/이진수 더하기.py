def solution(bin1, bin2):
    ans_10 = int(bin1, 2) + int(bin2, 2)
    ans_2 = ''
    while ans_10 >= 0:
        ans_10, mod = divmod(ans_10, 2)
        ans_2 += str(mod)
        if ans_10 == 0:
            break
    return ans_2[::-1]