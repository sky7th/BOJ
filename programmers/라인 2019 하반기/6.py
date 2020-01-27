from collections import defaultdict

n, s = input().strip().split(' ')
size = [0 for _ in range(10)]

for i in range(int(n)):
    a, nums = input().strip().split(' ')
    nums = list(nums)
    for num in nums:
        size[int(num)] = a

max_height = max(size)

for i in range(11):
    x = int(size[i])
    height = 2*x -1
    for i in range(height):
        if i == 0:
            print('.'*(x-1)+'#', )
        elif i < (height//2):
            print('.'*(x-1)+'#', )
        elif i == (height//2):
            print('.'*(x-1)+'#', )
        elif i < height-1:
            print('.'*(x-1)+'#', )
        elif i == height-1:
            print('.'*(x-1)+'#', )
