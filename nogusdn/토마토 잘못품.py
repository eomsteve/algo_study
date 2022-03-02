M, N, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N*H)]
dr = [0, 1, 0, -1, N, -N] # 우 하 좌 상 앞 뒤
dc = [1, 0, -1, 0, 0, 0]
for i in range(N*H):
    for j in range(M):
        if arr[i][j] == 1:
            r, c = i, j
            break
queue = []
queue.append((r, c))
while queue:
    r, c = queue.pop(0)
    for d in range(6):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N*H and 0 <= nc < M and arr[nr][nc] == 0:
            arr[nr][nc] = arr[r][c] + 1
            queue.append((nr, nc))

def solve():
    max_v = 0
    for i in range(N*H):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
            if arr[i][j] > max_v:
                max_v = arr[i][j]
    return max_v-1

print(solve())