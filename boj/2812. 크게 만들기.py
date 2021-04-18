standard_input = ['5 2', '54231']

N, K = map(int, input().split())
count_down = K
str_num = input()
stack = []

for c in str_num:
    while count_down > 0 and stack and stack[-1] < c:
        stack.pop()
        count_down -= 1
    
    stack.append(c)
    
print(''.join(stack[:N - K]))