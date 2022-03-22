N = int(input())
arr = [input() for _ in range(N)]
arr2 = []
for row in arr:
    arr2.append(row.replace('G', 'R'))

visited = [[0]*N for _ in range(N)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]
# 적록색약
def dfs(r, c, arr):
    stack = []
    stack.append((r, c))
    while stack:
        visited[r][c] = 1
        r, c = stack[-1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] == arr[r][c]:
                stack.append((nr, nc))
                break
        else:
            stack.pop()
cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, arr)
            cnt1 += 1

visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, arr2)
            cnt2 += 1

print(cnt1, cnt2)