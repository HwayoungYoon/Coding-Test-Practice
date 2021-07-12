# -*- coding: utf-8 -*-
"""
파이썬 기본 문법: 조건문
"""

""" if-elif-else """
score = 95
if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
else:
    print("학점: C")


""" 비교 연산자 """
# X == Y : 서로 같으면 참
# X != Y : 서로 다르면 참
# X > Y : X가 크면 참
# X < Y : Y가 크면 참
# X >= Y : X가 크거나 같으면 참
# X <= Y : Y가 크거나 같으면 참


""" 논리 연산자 """
# X and Y : 둘 다 참이어야 참
# X or Y : 둘 중 하나만 참이어도 참
# not X : X가 거짓이면 참


""" 기타 연산자 """
# X in 리스트 : 리스트 안에 X가 있으면 참
# X not in 문자열 : 문자열 안에 X가 있지 않으면 참


""" pass : 조건문의 값이 참이어도 아무것도 처리하지 않음 """
score = 95
if score >= 90:
    pass
else:
    print("학점: C")


""" 조건부 표현식(code 2) : code 1과 code 2의 실행 결과는 같음 """
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

# code 1
result = []
for i in a:
    if i not in remove_set:
        result.append(i)
print(result)

# code 2
result = [i for i in a if i not in remove_set]
print(result)
