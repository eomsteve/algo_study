import sys
sys.stdin = open('2751.txt', 'r')

T = int(input())
arr = []
for tc in range(T):
    arr.append(int(input()))

for i in range(len(arr)):
    min_arr = arr[i]
    min_idx = i
    for idx in range(i, len(arr)):
        if min_arr > arr[idx]:
            min_idx = idx
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for idx in arr:
    print(idx)