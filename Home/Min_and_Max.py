def min(*args, **kwargs):
    key = kwargs.get("key", None)

    if len(args) == 1:
        args = list(args[0])

    answer = args[0]
    for arg in args:
        if key is not None and key(answer) > key(arg) or key is None and answer > arg:
            answer = arg

    return answer


def max(*args, **kwargs):
    key = kwargs.get("key", None)

    if len(args) == 1:
        args = list(args[0])

    answer = args[0]
    for arg in args:
        if key is not None and key(answer) < key(arg) or key is None and answer < arg:
            answer = arg

    return answer


if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
