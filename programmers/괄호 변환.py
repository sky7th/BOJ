def solution(p):
    if p == '':
        return ''

    u, v = split_two_balance_gwalho(p)
    if is_correct_gwalho(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse_gwalho(u)


def split_two_balance_gwalho(p):
    count = 0
    for index, c in enumerate(p):
        if c == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return p[:index + 1], p[index + 1:]


def is_correct_gwalho(p):
    count = 0
    for c in p:
        if c == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0


def reverse_gwalho(p):
    return ''.join([')' if c=='(' else '(' for c in p[1:-1]])


print(solution("()))((()"))