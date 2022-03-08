# acmicpc.net/problem/2512
# 예산


N = int(input())
arr = list(map(int, input().split()))
max_val = int(input())

start = 0
end = max(arr)
# 최댓값이 되는 중앙값을 찾음
while start <= end:
    mid = (start+end)//2
    sum_val = 0
    # 최댓값을 넘는수가 있으면 그 값을 최댓값을 변환해 더함
    for i in range(N):
        if arr[i] <= mid:
            sum_val += arr[i]
        else:
            sum_val += mid
    if sum_val <= max_val:
        start = mid+1
    else:
        end = mid-1
print(end)
