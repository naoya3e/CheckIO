from functools import reduce

def checkio(number):
    return reduce(lambda a, b: a * b, [int(x) for x in str(number) if x != '0'])

if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
