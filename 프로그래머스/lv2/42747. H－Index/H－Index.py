def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = len(citations)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
        else:
            return answer