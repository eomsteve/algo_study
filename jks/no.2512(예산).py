N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr.sort()
is_find = False
while True:
    for i in range(len(arr)):
        my_sum = 0
        for j in range(i+1):
            my_sum += arr[j]
        my_sum += arr[i] * (len(arr) - i)
        if my_sum > M:
            for k in range(i):
                M -= arr[k]
            M = M//(len(arr) - i)
            is_find = True
            break
    if is_find:
        break
print(M)