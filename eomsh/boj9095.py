tc = int(input())

for test in range(1, tc+1):
    N = int(input())
    arr = [0] * 12
    arr[0] = 0
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    if N >= 4:
        for n in range(4, N+1):
            arr[n] = arr[n-1] + arr[n-2] + arr[n-3]
    print(arr[N])