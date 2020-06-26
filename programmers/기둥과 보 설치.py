PILLAR = 0
PLATE = 1
BUILD = 1
REMOVE = 0
FIELD_SIZE = 0


def solution(n, build_frame):
    global FIELD_SIZE
    FIELD_SIZE = n + 1
    field = []

    for x, y, structure, action in build_frame:
        if action == BUILD:
            build(field, x, y, structure)

        if action == REMOVE:
            remove(field, x, y, structure)

    return sorted(field, key=lambda x: (x[0], x[1], x[2]))


def build(field, x, y, structure):
    if can_located(field, x, y, structure):
        field.append([x, y, structure])


def can_located(field, x, y, structure):
    if structure == PILLAR:
        return is_floor(x, y) or is_pillar(field, x, y - 1) or is_plate(field, x, y) or is_plate(field, x - 1, y)

    elif structure == PLATE:
        return is_pillar(field, x, y - 1) or is_pillar(field, x + 1, y - 1) \
               or (is_plate(field, x - 1, y) and is_plate(field, x + 1, y))


def is_floor(x, y): return y == 0
def is_pillar(field, x, y): return is_in_field(x, y) and [x, y, PILLAR] in field
def is_plate(field, x, y): return is_in_field(x, y) and [x, y, PLATE] in field
def is_in_field(x, y): return 0 <= x < FIELD_SIZE and 0 <= y < FIELD_SIZE


def remove(field, x, y, structure):
    field.remove([x, y, structure])
    if not can_located_all_structure(field):
        field.append([x, y, structure])


def can_located_all_structure(field):
    for x, y, structure in field:
        if not can_located(field, x, y, structure):
            return False

    return True


print(solution(5,[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))