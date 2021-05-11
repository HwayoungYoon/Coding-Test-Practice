# -*- coding: utf-8 -*-
"""
2020 KAKAO Internship Test 1
"""

def distance(x1, y1, x2, y2):
    result = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    return result

def solution(numbers, hand):
    answer = ''
    left_x = 0
    left_y = 0
    right_x = 2
    right_y = 0
    for numbers in numbers:
        if numbers==1:
            answer += 'L'
            left_y = 3
        elif numbers==4:
            answer += 'L'
            left_y = 2
        elif numbers==7:
            answer += 'L'
            left_y = 1
        elif numbers==3:
            answer += 'R'
            right_y = 3
        elif numbers==6:
            answer += 'R'
            right_y = 2
        elif numbers==9:
            answer += 'R'
            right_y = 1
        elif numbers==2:
            dist_left = distance(left_x, left_y, 1, 3)
            dist_right = distance(right_x, right_y, 1, 3)
            if dist_left > dist_right:
                answer += 'R'
            elif dist_left < dist_right:
                answer += 'L'
            else:
                if hand=='left':
                    answer += 'L'
                else:
                    answer += 'R'
        elif numbers==5:
            dist_left = distance(left_x, left_y, 1, 2)
            dist_right = distance(right_x, right_y, 1, 2)
            if dist_left > dist_right:
                answer += 'R'
            elif dist_left < dist_right:
                answer += 'L'
            else:
                if hand=='left':
                    answer += 'L'
                else:
                    answer += 'R'
        elif numbers==8:
            dist_left = distance(left_x, left_y, 1, 1)
            dist_right = distance(right_x, right_y, 1, 1)
            if dist_left > dist_right:
                answer += 'R'
            elif dist_left < dist_right:
                answer += 'L'
            else:
                if hand=='left':
                    answer += 'L'
                else:
                    answer += 'R'        
        else:
            dist_left = distance(left_x, left_y, 1, 0)
            dist_right = distance(right_x, right_y, 1, 0)
            if dist_left > dist_right:
                answer += 'R'
            elif dist_left < dist_right:
                answer += 'L'
            else:
                if hand=='left':
                    answer += 'L'
                else:
                    answer += 'R'
    return answer

numbers = [9,4,2,0]
hand = 'right'
solution(numbers, hand)
