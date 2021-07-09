# -*- coding: utf-8 -*-
"""
2021 KAKAO Internship Test 2
"""

def solution(places):
    answer = []
    for i in range(5):
        if any("PP" in s for s in places[i]) or any("POP" in s for s in places[i]):
            answer.append(0)
        else:
            answer.append(1)
    return answer
places = [["PPOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)



aat = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]

import numpy as np
np.array(["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"])
aa = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
list(aa[0])
aa[0][0]
list(aa[0][0])


def solution(places):
    answer = []
    for i in range(5):
        place1 = []
        place1.append(list(places[0][i]))
        place1 = np.array(place1)
        place2 = []
        place2.append(list(places[1][i]))
        place2 = np.array(place2)
        place3 = []
        place3.append(list(places[2][i]))
        place3 = np.array(place3)
        place4 = []
        place4.append(list(places[3][i]))
        place4 = np.array(place4)
        place5 = []
        place5.append(list(places[4][i]))
        place5 = np.array(place5)
        if any("PP" in s for s in place1):
            answer.append(0)
        else:
            answer.append(1)
    return answer


for i in range(5):
    place1 = []
    place1.append(list(places[0][i]))
    place1 = np.array(place1)
    print(place1)
for i in range(5):
    place2 = []
    place2.append(list(places[1][i]))
    place2 = np.array(place2)
for i in range(5):
    place3 = []
    place3.append(list(places[2][i]))
    place3 = np.array(place3)
for i in range(5):
    place4 = []
    place4.append(list(places[3][i]))
    place4 = np.array(place4)
for i in range(5):
    place5 = []
    place5.append(list(places[4][i]))
    place5 = np.array(place5)



arr = np.array(aa)
print(aa)



