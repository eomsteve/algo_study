M, N, H = map(int, input().split())
arr = []
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))
    arr.append(temp)

# print(arr)

dr = [0, 1, 0, -1, 0, 0] # 우 하 좌 상 앞 뒤
dc = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = []
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                queue.append((k, i, j))

while queue:
    z, r, c = queue.pop(0)
    for d in range(6):
        nz = z + dz[d]
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and 0 <= nz < H and arr[nz][nr][nc] == 0:
            arr[nz][nr][nc] = arr[z][r][c] + 1
            queue.append((nz, nr, nc))
# print(arr)
#
def solve():
    max_v = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 0:
                    return -1
                if arr[k][i][j] > max_v:
                    max_v = arr[k][i][j]
    return max_v-1

print(solve())