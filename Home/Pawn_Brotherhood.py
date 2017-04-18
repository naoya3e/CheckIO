def safe_pawns(pawns):
    safe = 0

    for pawn in pawns:
        left  = chr(ord(pawn[0])-1)+str(int(pawn[1])-1)
        right = chr(ord(pawn[0])+1)+str(int(pawn[1])-1)

        if left in pawns or right in pawns:
            safe += 1

    return safe

if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
