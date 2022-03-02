N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
r, c = 0, 0 # 시작 위치
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt = 1
min_v = 9999
# print(arr)
def solve(r,c):
    global cnt
    global min_v
    visited[r][c] = 1
    if r == N-1 and c == M-1:
        if cnt < min_v:
            min_v = cnt
            return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and not visited[nr][nc]:
            cnt += 1
            solve(nr, nc)
            cnt -= 1
            visited[nr][nc] -= 1
solve(r,c)
print(min_v)