N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_v = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            arr_sum = arr[i] + arr[j] + arr[k]
            if arr_sum <= M and arr_sum > max_v:
                max_v = arr_sum
print(max_v)