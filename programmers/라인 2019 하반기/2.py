from itertools import permutations

input_list = list(map(str, input().strip().split(' ')))
k = input()
print(len(input_list))

perm = permutations(input_list, 3)
res = list(map(''.join, permutations(input_list, 3)))
res.sort()
print(res[int(k)-1])