def solution(numbers):
    sort_num = sorted(numbers)
    p_num = sort_num[0]*sort_num[1]
    m_num = sort_num[-1]*sort_num[-2]
    return max(p_num, m_num)