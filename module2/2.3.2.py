import itertools

def is_true(a):
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for _ in range(3, a // 2, 2):
        if a % _ == 0:
            return False
    return True

def primes():
    a = 2
    while True:
        if is_true(a):
            yield a
        a += 1



print(list(itertools.takewhile(lambda x : x <= 31, primes())))


