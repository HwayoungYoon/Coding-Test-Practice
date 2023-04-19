def solution(rsp):
    trans = rsp.maketrans('025', '502')
    return rsp.translate(trans)