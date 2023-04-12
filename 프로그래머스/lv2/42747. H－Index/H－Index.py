def solution(citations):
    citations = sorted(citations, reverse=True)
    if min(citations) >= len(citations):
        return len(citations)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i