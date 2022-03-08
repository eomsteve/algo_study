# 10026 / 적록색약
# https://www.acmicpc.net/problem/10026

from collections import deque

# 상하좌우 탐색을 위한 변수
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            # 4방향을 탐색해서 같은색이라면 1
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == arr[x][y] and c[nx][ny] == 0:
                    q.append([nx, ny])
                    c[nx][ny] = 1

N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
c = [[0]*N for _ in range(N)]
q = deque()

cnt = 0
for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'
c = [[0]*N for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)

### 접근 방법
# bfs를 이용하여 0으로 된 N*N 배열에서 같은색인부분을 1로 덮어주고 cnt를 1 늘려주는 작업을 반복 => 적록색약은 R을 G로 바꿔 재반복