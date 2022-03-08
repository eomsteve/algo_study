from collections import deque
N, M = map(int, input().split())
q = deque()
maze = [list(map(int, list(input()))) for _ in range(N)]
q.append((0, 0))
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = 0

while q:
    r, c = q.popleft()
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if maze[nr][nc] == 1:
                maze[nr][nc] = maze[r][c] + 1
                q.append((nr, nc))

print(maze[N-1][M-1])