T = int(input())

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def dfs(r, c):
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1:
                arr[nr][nc] = 0
                dfs(nr, nc)


for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)