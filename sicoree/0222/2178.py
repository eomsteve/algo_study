# 2178 / 미로찾기
# https://www.acmicpc.net/problem/2178

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

queue = [(0,0)]

while queue:
    x, y = queue.pop(0)

    if x == N - 1 and y == M - 1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + di[i]
        ny = y + dj[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and arr[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))