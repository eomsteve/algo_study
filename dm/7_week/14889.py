# https://www.acmicpc.net/problem/14889
# 스타트와 링크


def start_t(idx):
    if idx == N//2:
        team(select)
        return
    for i in range(N):
        if not v[i]:
            if idx != 0 and select[idx-1] > i:
                    continue
            select[idx] = i
            v[i] = 1
            start_t(idx+1)
            v[i] = 0


def team(a):
    global min_v
    t1 = []
    t2 = []
    for i in range(N):
        if i in a:
            t1.append(i)
        else:
            t2.append(i)
    t1_s = t2_s = 0
    for a in range(N//2):
        for b in range(a+1, N//2):
            t1_s += arr[t1[a]][t1[b]] + arr[t1[b]][t1[a]]
            t2_s += arr[t2[a]][t2[b]] + arr[t2[b]][t2[a]]
    sum_v = abs(t1_s-t2_s)
    if min_v > sum_v:
        min_v = sum_v
            

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [0]*N
select = [0]*(N//2)
min_v = 101
start_t(0)
print(min_v)