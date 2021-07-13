# -*- coding: utf-8 -*-
"""
파이썬 기본 문법: 반복문
"""

""" while """
# 1부터 9까지의 정수 중 홀수끼리의 합
i = 1
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1


""" for """
# 1부터 9까지 모든 정수의 합
result = 0
for i in range(1,10):
    result += i


""" range : range(시작값, 끝값+1), 시작값이 생략된 경우에는 0부터 시작 """
scores = [90,85,77,65,97]
for i in range(5):
    if scores[i] >=80:
        print(i + 1, "번 학생은 합격입니다.")


""" continue : 반복문의 처음으로 되돌리기 """
scores = [90,85,77,65,97]
cheating_list = {2,4}
for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >=80:
        print(i + 1, "번 학생은 합격입니다.")
