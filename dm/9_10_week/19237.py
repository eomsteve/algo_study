# https://www.acmicpc.net/problem/19237
# 어른 상어

from copy import deepcopy

def move_shark(v):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        # 상어 냄새 빠짐 현상
        for i in range(N):
            for j in range(N):
                if v[i][j][1]:
                    v[i][j][1] -= 1
        nv = deepcopy(v)
        # 상어의 이동
        for i in range(1, M+1):
            cr, cc, cd = shark[i]
            if shark[i] == (-1, -1, -1):
                continue
            for d in range(4):
                nr = cr+dr[priority_d[i][cd][d]]
                nc = cc+dc[priority_d[i][cd][d]]
                if 0 <= nr < N and 0 <= nc < N:
                    # 빈공간이 있으면 상어가 들어감
                    if v[nr][nc] == [0, 0]:
                        # 만약 탐색한곳이 갓 상어가 위치하면 상어끼리 비교해봄
                        if nv[nr][nc][1] == k:
                            shark[i] = (-1, -1, -1)
                            i = nv[nr][nc][0]
                            dd = shark[i][2]
                            break
                        else:
                            dd = priority_d[i][cd][d]
                            break
            else:
                # 그것도 없으면, 자기 냄새로 돌아감
                for d in range(4):
                    nr = cr+dr[priority_d[i][cd][d]]
                    nc = cc+dc[priority_d[i][cd][d]]
                    if 0 <= nr < N and 0 <= nc < N and  v[nr][nc][0] == i:
                        dd = priority_d[i][cd][d]
                        break
            shark[i] = (nr, nc, dd)
            nv[nr][nc] = [i, k]
        for i in range(N):
            for j in range(N):
                if nv[i][j][0] and not nv[i][j][1]:
                    nv[i][j] = [0, 0]
        v = nv
        for i in range(2, M+1):
            if shark[i] != (-1, -1, -1):
                break
        else:
            return cnt
    return -1


N, M, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
shark_d = list(map(int, input().split()))
priority_d = []
priority_d.append([(0, 0, 0, 0)]*M)
for _ in range(M):
    tmp = [(0, 0, 0, 0)]
    for _ in range(4):
        tmp.append(tuple(map(int, input().split())))
    priority_d.append(tmp)
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)
shark = [(-1, -1, -1) for _ in range(M+1)]
v = [[[0]*2 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            shark[arr[i][j]] = (i, j, shark_d[arr[i][j]-1])
            v[i][j] = [arr[i][j], k]
print(move_shark(v))
