# https://www.acmicpc.net/problem/19236
# 청소년 상어


from copy import deepcopy

def sol(shark, arr, loc):
    global max_fish
    # 물고기 이동
    for i in range(1, 17):
        if loc[i] != (-1, -1):
            fr, fc = loc[i]
            cd = arr[fr][fc][1]
            for z in range(8):
                d = ((cd-1)+z)%8+1
                nfr = fr + dr[d]
                nfc = fc + dc[d]
                if 0 <= nfr < 4 and 0 <= nfc < 4 and arr[nfr][nfc][0] != -1:
                    arr[fr][fc] = (i, d)
                    # 물고기 위치 업데이트
                    arr[fr][fc], arr[nfr][nfc] = arr[nfr][nfc], arr[fr][fc]
                    if arr[fr][fc] != (0, 0):
                        loc[arr[fr][fc][0]] = (fr, fc)
                    loc[i] = (nfr, nfc)
                    break
    # 상어의 이동
    sr, sc, sum_fish, d = shark
    for z in range(1, 4):
        nr = sr + dr[d]*z
        nc = sc + dc[d]*z
        narr, nloc = deepcopy(arr), deepcopy(loc)
        if 0 <= nr < 4 and 0 <= nc < 4:
            if narr[nr][nc] == (0, 0):
                continue
            shark = (nr, nc, sum_fish+narr[nr][nc][0], narr[nr][nc][1])
            narr[sr][sc] = (0, 0)
            nloc[arr[nr][nc][0]] = (-1, -1)
            narr[nr][nc] = (-1, narr[nr][nc][1])
            sol(shark, narr, nloc)
        else:
            break
    max_fish = max(max_fish, shark[2])

dr = (0, -1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 0, -1, -1, -1, 0, 1, 1, 1)
# 수족관 물고기 위치
loc = [(-1,-1)]*17
arr = [[(0, 0) for _ in range(4)] for _ in range(4)]
for i in range(4):
    fish = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = (fish[j*2], fish[j*2+1])
        loc[fish[j*2]] = (i, j)
# 상어가 들어옴
shark = (0, 0, arr[0][0][0], arr[0][0][1])
loc[arr[0][0][0]] = (-1, -1)
arr[0][0] = (-1, arr[0][0][1])
max_fish = 0
sol(shark, arr, loc)
print(max_fish)
