import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    num = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        elif len(scoville) > 1:
            x1 = heapq.heappop(scoville)
            x2 = heapq.heappop(scoville)
            heapq.heappush(scoville, x1+x2*2)
            num += 1
    return num