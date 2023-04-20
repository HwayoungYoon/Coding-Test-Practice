from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    ans = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    answer = [ans.numerator, ans.denominator]
    return answer