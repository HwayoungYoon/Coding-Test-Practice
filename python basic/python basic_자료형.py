# -*- coding: utf-8 -*-
"""
파이썬 기본 문법: 자료형
"""

""" 수 자료형 """
# 양의 정수
a = 100
# 음의 정수
b = -7

# 양의 실수
a = 157.
# 음의 실수
b = -.2

# 지수 표현
a = 23e4

# 소수점 반올림
round(123.456, 2)

# 연산
print(a / b) # 나누기
print(a % b) # 나머지
print(a // b) # 몫


""" 리스트 자료형 """
a = [1,2,3,4,5]

# 빈 리스트 선언
a = list()
a = []

# 크기가 n이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n

# 리스트 초기화: 0부터 19까지 중 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
# 리스트 초기화: 1부터 9까지 수의 제곱을 포함하는 리스트
array = [i * i for i in range(1,10)]

# n X m 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]

# 리스트에 원소 삽입
a.append(2)
# 오름차순 정렬
a.sort()
# 내림차순 정렬
a.sort(reverse = True)
# 리스트 원소 뒤집기
a.reverse()
# n번 인덱스에 x 추가
n = 2
x = 4
a.insert(n, x)
# 특정 값을 만족하는 데이터 개수
a.count(2)
# 특정 값 데이터 삭제
a.remove(1)
# 특정 값들을 만족하는 데이터 삭제
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]


""" 문자열 자료형 """
# ' or " 문자열에 포함: \' or \"
data = "Don't you know \"Python\"?"

# 문자열 덧셈
a = "Hello"
b = "World"
print(a + " " + b)
# 문자열 곱셈
a = "String"
print(a * 3)
# 인덱스, 슬라이싱
a = "ABCDEF"
print(a[2:4])


""" 튜플 자료형 """
a = (1,2,3,4)
## 리스트와 비슷하지만 한 번 선언된 값의 변경 불가능


""" 사전 자료형 """
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 특정한 원소 확인
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])


""" 집합 자료형 """
# 초기화 방법
data = set([1,1,2,3,4,4,5])
data = {1,1,2,3,4,4,5}

# 연산
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# 새로운 원소 추가
data.add(4)
# 새로운 원소 여러 개 추가
data.update([5,6])
# 특정한 값을 갖는 원소 삭제
data.remove(3)
