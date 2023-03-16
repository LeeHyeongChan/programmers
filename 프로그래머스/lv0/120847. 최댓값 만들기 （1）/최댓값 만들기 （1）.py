import numpy as np
def solution(numbers):
    s = sorted(numbers)
    answer = s[-1] * s[-2]
    return answer