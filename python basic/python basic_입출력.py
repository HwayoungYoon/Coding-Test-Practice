# -*- coding: utf-8 -*-
"""
파이썬 기본 문법: 입출력
"""

""" 입력 """
# input() : 한 줄의 문자열 입력
# int() : 문자열을 정수로 변환
# list(map(int, input().split()))
# : 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장


""" 입력을 위한 소스코드 """
# 데이터 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)


""" 공백을 기준으로 구분하여 적은 수의 데이터 입력 """
# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())
print(n, m, k)


""" readline() : 입력의 개수가 많을 경우 """
import sys
data = sys.stdin.readline().rstrip()
print(data)


""" 출력 """
# print() : 표준 출력, 출력 이후 줄 바꿈 수행


""" 문자열 출력 """
# 문자열 자료형끼리만 더하기가 가능하므로 answer을 문자열로 바꿔야 함
answer = 7
print("정답은" + answer + "입니다.")

# 변수를 문자열로 바꾸어 출력
print("정답은 " + str(answer) + "입니다.")

# 각 변수를 ,로 구분하여 출력 : 값들 사이에 공백 삽입
print("정답은", str(answer), "입니다.")

# f-string 문법
print(f"정답은 {answer}입니다.")
