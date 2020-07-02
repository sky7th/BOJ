from collections import deque
from itertools import permutations
import re


def solution(expression):
    result = 0
    for operator_order in permutations(['*', '+', '-']):
        numbers = deque([int(number) for number in re.findall('[0-9]+', expression)])
        operators = deque(re.findall('[\W]+', expression))

        for priority_operator in operator_order:
            numbers, operators = operate_to_priority_operator(priority_operator, numbers, operators)

        result = max(result, abs(numbers[0]))

    return result


def operate_to_priority_operator(priority_operator, numbers, operators):
    number_stack = deque()
    operator_stack = deque()
    number_stack.append(numbers.popleft())

    while operators:
        now_number = numbers.popleft()
        now_operator = operators.popleft()

        if now_operator == priority_operator:
            operated_number = operate(priority_operator, number_stack.pop(), now_number)
            number_stack.append(operated_number)
            continue

        number_stack.append(now_number)
        operator_stack.append(now_operator)

    return number_stack, operator_stack


def operate(operator, num1, num2):
    if operator == '*':
        return num1*num2
    if operator == '+':
        return num1+num2
    if operator == '-':
        return num1-num2


print(solution("100-200*300-500+20"))

