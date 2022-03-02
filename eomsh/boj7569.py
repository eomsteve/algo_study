from sys import stdin
from collections import deque
input = stdin.readline
M, N, Z = map(int, input().split())


def bfs(queue, cnt):
    while queue:
        cnt += 1
        dr, dc, dz = [0, -1, 0, 1, 0, 0], [1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, -1]
        for _ in range(len(queue)):
            z, r, c = queue.popleft()
            for d in range(6):
                nr = r + dr[d]
                nc = c + dc[d]
                nz = z + dz[d]
                if 0 <= nr < N and 0 <= nc < M and 0<= nz < Z:
                    if arr[nz][nr][nc] == 0:
                        queue.append((nz, nr, nc))
                        arr[nz][nr][nc] = 1
    return cnt


q = deque()
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(Z)]

for i in range(N):
    for j in range(M):
        for h in range(Z):
            if arr[h][i][j] == 1:
                q.append((h, i, j))

result = bfs(q, -1)

for i in range(N):
    for j in range(M):
        for h in range(Z):
            if arr[h][i][j] == 0:
                result = -1

print(result)
