# https://www.acmicpc.net/problem/14500
# 테트로미노


import sys
input = sys.stdin.readline

def bk(cr, cc, idx, sum_v):
    global max_v
    if idx == 3:
        max_v = max(max_v, sum_v)
        return
    if max_v >= sum_v + max_val * (3 - idx):
        return
    if cr == i+2 and cc == j:
        nr = cr - 1
        for k in range(2):
            nc = cc + (-1)**(k)
            if 0 <= nr < N and 0 <= nc < M:
                bk(nr, nc, idx+1, sum_v+arr[nr][nc])
    if cr == i and cc == j+2:
        nc = cc - 1
        for k in range(2):
            nr = cr + (-1)**(k)
            if 0 <= nr < N and 0 <= nc < M:
                bk(nr, nc, idx+1, sum_v+arr[nr][nc])
    for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr = cr + d[0]
        nc = cc + d[1]
        if 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
            v[nr][nc] = 1
            bk(nr, nc, idx+1, sum_v+arr[nr][nc])
            v[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
max_val = max(map(max, arr))
max_v = 0
for i in range(N):
    for j in range(M):
        v[i][j] = 1
        bk(i, j, 0, arr[i][j])
        v[i][j] = 0
print(max_v)
