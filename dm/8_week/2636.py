# https://www.acmicpc.net/problem/2636
# 치즈


from collections import deque


def bfs(loc):
    v = [[0]*M for _ in range(N)]
    v[loc[0]][loc[1]] = 1
    queue = deque()
    queue.append(loc)
    while queue:
        s = queue.popleft()
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = s[0] + d[0]
            nc = s[1] + d[1]
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and not arr[nr][nc]:
                v[nr][nc] = v[s[0]][s[1]] + 1
                queue.append((nr, nc))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not v[i][j]:
                for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nr = i + d[0]
                    nc = j + d[1]
                    if v[nr][nc]:
                        arr[i][j] = 0
                        cnt += 1
                        break
    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
hour = 0
pre_cheese = 0
while True:
    cheese = bfs((0, 0))
    if cheese == 0:
        print(hour)
        print(pre_cheese)
        break
    hour += 1
    pre_cheese = cheese
