# -*- coding: utf-8 -*-
"""
파이썬 기본 문법: 표준라이브러리
"""

""" 파이썬 표준 라이브러리 """
# https://docs.python.org/ko/3/library/index.html


""" 내장 함수 : 기본 내장 라이브러리(ex. input(), print(), sorted()) """
# sum() : 리스트와 같은 iterable 객체(사전 자료형, 튜플 자료형 등)의 모든 원소의 합
result = sum([1,2,3,4,5])
print(result)

# min() : 최솟값
result = min(7,3,5,2)
print(result)

# max() : 최댓값
result = max(7,3,5,2)
print(result)

# eval() : 수식 계산 결과 반환
result = eval("(3+5)*7")
print(result)

# sorted() : iterable 객체 정렬(오름차순이 default, 내림차순은 reverse = True 옵션)
result = sorted([9,1,8,5,4])
print(result)
result = sorted([9,1,8,5,4], reverse = True)
print(result)







""" itertools : 반복되는 형태의 데이터 처리, 순열과 조합 라이브러리 제공 """















""" heapq : 힙(Heap) 기능 제공, 우선순위 큐 기능 구현에 사용 """















""" bisect : 이진 탐색(Binary Search) 기능 제공 """















""" collections : 덱(deque), 카운터(Counter) 등의 자료구조 포함 """















""" math : 필수적인 수학적 기능 제공, !, 제곱근, 최대공약수, 삼각함수 등의 함수와 상수 pi """




















