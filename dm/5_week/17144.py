# https://www.acmicpc.net/problem/17144
# 미세먼지 안녕!


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
for _ in range(T):
# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
    diff = []
    diff_len = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] and arr[i][j] != -1:
                diff.append((i, j, arr[i][j]))
                cnt = 0
                for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nr = i + d[0]
                    nc = j + d[1]
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                        cnt += 1
                diff_len.append(cnt)
    for i in range(len(diff)):
        arr[diff[i][0]][diff[i][1]] -= (diff[i][2]//5)*diff_len[i]
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = diff[i][0] + d[0]
            nc = diff[i][1] + d[1]
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                arr[nr][nc] += diff[i][2]//5
    # 2. 공기청정기가 작동한다.
    # 공기청정기에서는 바람이 나온다.
    # 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    # 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    # 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
    wd = []
    dir1 = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    dir2 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(R):
        if arr[i][0] == -1:
            wd.append(i)

    def wind(cr, cc, dir):
        r, c = cr, cc
        tmp = 0
        for d in dir:
            nr = r + d[0]
            nc = c + d[1]
            while 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                if not (0 <= nr+d[0] < R and 0 <= nc+d[1] < C and arr[nr][nc] != -1):
                    r = nr
                    c = nc
                tmp2 = arr[nr][nc]
                arr[nr][nc] = tmp
                tmp = tmp2
                nr = nr+d[0]
                nc = nc+d[1]
    
    
    wind(wd[0], 0, dir1)
    wind(wd[1], 0, dir2)
    sum_val = 0
    for a in arr:
        sum_val += sum(a)
print(sum_val+2)