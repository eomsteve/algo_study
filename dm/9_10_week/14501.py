# https://www.acmicpc.net/problem/14501
# 퇴사

def bk(idx, day, sum_v):
    global max_v
    if day < 0:
        return
    if idx == N:
        max_v = max(max_v, sum_v)
        return
    bk(idx+1, day-1, sum_v)
    bk(idx+arr[idx][0], day-arr[idx][0], sum_v+arr[idx][1])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
bk(0, N, 0)
print(max_v)
