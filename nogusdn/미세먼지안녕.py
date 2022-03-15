R, C, T = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(R)]
arr = [[0]*C for _ in range(R)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for i in range(R):
    if dust[i][0] == -1:
        air1 = i
        air2 = i+1
        break
arr[air1][0] = -1
arr[air2][0] = -1

def solve1():
    for r in range(R):
        for c in range(C):
            if dust[r][c] and dust[r][c] != -1: # 공기청정기가 아니고 먼지가 있으면
                result = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and dust[nr][nc] != -1:
                        arr[nr][nc] += dust[r][c]//5
                        result += dust[r][c]//5
                arr[r][c] += dust[r][c] - result

def solve2():
    r = air1
    c = 0
    d = 0 # 처음은 오른쪽부터
    tmp = 0
    while True:
        r += dr[d]
        c += dc[d]
        if r == air1 and c == 0:
            break
        if r < 0 or r >= R or c < 0 or c >= C:
            d = (d+3) % 4
            continue
        arr[r][c], tmp = tmp, arr[r][c]

def solve3():
    r = air2
    c = 0
    d = 0  # 처음은 오른쪽부터
    tmp = 0
    while True:
        r += dr[d]
        c += dc[d]
        if r == air2 and c == 0:
            break
        if r < 0 or r >= R or c < 0 or c >= C:
            d = (d + 1) % 4
            continue
        arr[r][c], tmp = tmp, arr[r][c]

for _ in range(T):
    solve1()
    solve2()
    solve3()
result = 0
for row in arr:
    print(row)
    result += sum(row)
print(result+2)