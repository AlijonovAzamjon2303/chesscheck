def pawn_check(x1, y1, x2, y2):
    return x1 == x2 and y2 - y1 == 1

def rook_check(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2


print(rook_check(1, 1, 8, 2))