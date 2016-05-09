
def point_col(position, rect):
    x, y = position
    if x < rect.x:
        return False
    if x > rect.x + rect.w:
        return False
    if y < rect.y:
        return False
    if y > rect.y + rect.h:
        return False
    return True
