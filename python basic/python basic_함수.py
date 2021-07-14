# -*- coding: utf-8 -*-
"""
파이썬 기본 문법: 함수
"""

""" def & return """
# def 함수명(매개변수):
#     실행할 소스코드
#     return 반환값
def add(a,b):
    return a+b


""" return을 생략하는 경우 : 함수 안에서 결과를 출력할 때 """
def add(a,b):
    print('함수의 결과:', a+b)


""" global : 함수 밖의 변수 데이터 변경 """
a = 0
def func():
    global a
    a += 1


""" 람다 표현식 """
# 위에서 정의한 add() 메서드와 동일한 결과를 나타내는 람다 표현식
print((lambda a,b: a+b)(3,7))
