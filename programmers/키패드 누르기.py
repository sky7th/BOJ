LEFT_NUMBERS = [1, 4, 7]
RIGHT_NUMBERS = [3, 6, 9]
LEFT_HAND = 0
RIGHT_HAND = 1
LEFT_HANDED = 'left'
RIGHT_HANDED = 'right'
STAR = 10
SHARP = 12
ZERO = 0


def solution(numbers, handed):
    left, right = STAR, SHARP
    result = ''

    for number in numbers:
        if number == 0:
            number = ZERO

        if number in LEFT_NUMBERS:
            hand = LEFT_HAND

        elif number in RIGHT_NUMBERS:
            hand = RIGHT_HAND
        else:
            hand = find_closest_hand_to_mid_number(number, left, right, handed)

        if hand == LEFT_HAND:
            left = number
            result += 'L'
        else:
            right = number
            result += 'R'

    return result


def find_closest_hand_to_mid_number(mid, left, right, handed):
    if get_distance(mid, left) < get_distance(mid, right):
        return LEFT_HAND

    elif get_distance(mid, left) > get_distance(mid, right):
        return RIGHT_HAND

    else:
        if handed == LEFT_HANDED:
            return LEFT_HAND
        else:
            return RIGHT_HAND


def get_distance(spot1, spot2):
    spot1_y, spot1_x = divmod(spot1 - 1, 3)
    spot2_y, spot2_x = divmod(spot2 - 1, 3)

    return abs(spot1_y - spot2_y) + abs(spot1_x - spot2_x)


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
