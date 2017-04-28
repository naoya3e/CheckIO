OPEN = ('{', '(', '[')
CLOSE = ('}', ')', ']')

def checkio(expression):
    stack = []

    for c in expression:
        if c in OPEN:
            stack.append(c)
        if c in CLOSE:
            if len(stack) <= 0:
                return False
            o = stack.pop()
            if OPEN.index(o) != CLOSE.index(c):
                return False

    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
