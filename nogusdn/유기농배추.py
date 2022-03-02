T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0]* M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        arr[r][c] = 1

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def bfs(r, c):
        queue = []
        queue.append((r, c))
        while queue:
            r, c = queue.pop(0)
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    queue.append((nr, nc))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)