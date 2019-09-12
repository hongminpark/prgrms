#https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations

def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def solution(numbers):
    result = set()
    for i in range(1, len(numbers) + 1):
        p = permutations(numbers, i)
        result |= {int("".join(n)) for n in p}
    return sum([1 for n in list(result) if is_prime(n)])
