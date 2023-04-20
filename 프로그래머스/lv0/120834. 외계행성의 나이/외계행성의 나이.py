def solution(age):
    age_t = str(age).maketrans('0123456789', 'abcdefghij')
    return str(age).translate(age_t)