N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
r, c = 0, 0
queue = []
queue.append((r, c))

dr = [0,1,0,-1]
dc = [1,0,-1,0]
while queue:
    r, c = queue.pop(0)
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
            queue.append((nr, nc))
            maze[nr][nc] = maze[r][c] + 1
print(maze[N-1][M-1])