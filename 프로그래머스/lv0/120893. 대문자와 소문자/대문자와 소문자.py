def solution(my_string):
    my_s = list(my_string)
    for i in range(len(my_string)):
        if my_s[i].isupper() == True:
            my_s[i] = my_s[i].lower()
        else:
            my_s[i] = my_s[i].upper()
    return ''.join(my_s)

# my_string.swapcase()