# https://www.acmicpc.net/problem/10026
# 적록색약

import sys
from collections import deque
input = sys.stdin.readline


# 일반인 시선 bfs
def bfs(location, key):
    queue.append(location)
    v[location[0]][location[1]] = 1
    while queue:
        loc = queue.popleft()
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = loc[0] + d[0]
            nc = loc[1] + d[1]
            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and arr[nr][nc] == key:
                v[nr][nc] = v[loc[0]][loc[1]] + 1
                queue.append((nr, nc))
# 적록색약인 경우 bfs(R과 G를 합쳐서 bfs를 적용)
def bfs2(location, key):
    queue.append(location)
    v2[location[0]][location[1]] = 1
    while queue:
        loc = queue.popleft()
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = loc[0] + d[0]
            nc = loc[1] + d[1]
            if key == 0:
                if 0 <= nr < N and 0 <= nc < N and not v2[nr][nc] and (arr[nr][nc] == 'R' or arr[nr][nc] == 'G'):
                    v2[nr][nc] = v2[loc[0]][loc[1]] + 1
                    queue.append((nr, nc))
            else:
                if 0 <= nr < N and 0 <= nc < N and not v2[nr][nc] and (arr[nr][nc] == 'B'):
                    v2[nr][nc] = v2[loc[0]][loc[1]] + 1
                    queue.append((nr, nc))

N = int(input())
arr = [list(input()) for _ in range(N)]
# 일반인 경우 방문 행렬
v = [[0 for _ in range(N)] for _ in range(N)]
# 적록색약인 경우 방문 행렬
v2 = [[0 for _ in range(N)] for _ in range(N)]
# list로 하면 시간초과가 생김 deque로 해야함
queue = deque()
# 한번 serch 될 때마다 cnt값을 증가시켜줌
cnt = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if (arr[i][j] == 'R' or arr[i][j] == 'G'):
            if not v2[i][j]:
                bfs2((i, j), 0)
                cnt2 += 1
            if arr[i][j] == 'R' and not v[i][j]:
                bfs((i, j), arr[i][j])
                cnt += 1
            elif arr[i][j] == 'G' and not v[i][j]:
                bfs((i, j), arr[i][j])
                cnt += 1
        else:
            if not v2[i][j]:
                bfs2((i, j), 1)
                cnt2 += 1
            if not v[i][j]:
                bfs((i, j), arr[i][j])
                cnt += 1
print(cnt, cnt2)