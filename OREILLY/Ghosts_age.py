def fib(n=10000):
    fibs = [0, 1, 2]

    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])

    return fibs

FIBONACCI = fib()

def checkio(opacity):
    v = 10000

    for year in range(5000):
        v += -year if year in FIBONACCI else 1
        if v == opacity:
            return year

if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
