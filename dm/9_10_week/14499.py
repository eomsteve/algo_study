# https://www.acmicpc.net/problem/14499
# 주사위 굴리기


N, M, X, Y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))
dr = [[-1, -1], [0, 1], [0, -1], [-1, 0], [1, 0]]
dice = [0]*7
# 현재위치: (1, 2, -3) 
# 동:(-3, 2, -1) 서:(3, 2, 1) 북: (-2, 1, -3) 남:(2, -1, -3) 
# (-2, 1, -3)
# (-3, 1, 2) (3, -2, 1) (-1, -2, -3) (1, 2, -3) 
d_loc = (1, 2, -3)
idx, r, c = 0, X, Y
while idx < K:
    d = cmd[idx]
    idx += 1
    nr, nc = r+dr[d][0], c+dr[d][1]
    if 0 <= nr < N and 0 <= nc < M:
        if d == 1:
            d_loc = (d_loc[2], d_loc[1], -d_loc[0])
        elif d == 2:
            d_loc = (-d_loc[2], d_loc[1], d_loc[0])
        elif d == 3:
            d_loc = (-d_loc[1], d_loc[0], d_loc[2])
        else:
            d_loc = (d_loc[1], -d_loc[0], d_loc[2])
        
        if arr[nr][nc] == 0:
            arr[nr][nc] = dice[-d_loc[0]]
        else:
            dice[-d_loc[0]] = arr[nr][nc]
            arr[nr][nc] = 0
        r, c = nr, nc
        print(dice[d_loc[0]])
