import sys
sys.stdin = open('10773.txt', 'r')

arr = []
T = int(input())
for tc in range(T):
    val = int(input())
    if val == 0:
        arr.pop()
    else:
        arr.append(val)

sum_arr = 0
for idx in arr:
    sum_arr += idx

print(sum_arr)