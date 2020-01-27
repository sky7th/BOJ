N = int(input())
input_list = list(map(int, input().strip().split(' ')))
subway = list()
for i in range(len(input_list)):
    if input_list[i] == 1:
        subway.append(i)
print(subway)
res = 0
for i in range(len(subway)):
    if i == 0:
        mx = subway[i+1]-subway[i]
    elif i == len(subway)-1:
        mx = subway[i]-subway[i-1]
    else:
        mx = max(subway[i+1]-subway[i], subway[i]-subway[i-1])
    if res < mx:
        res = mx

print(res//2)