# 16236 / 뚜루루뚜루
# https://www.acmicpc.net/problem/16236

import sys
from collections import deque

# 상 좌 우 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def BFS(x, y):
    global result, size

    q = deque()
    q.append([x, y])

    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    
    xy_q = deque()
    tx, ty = x, y

    while q:
        c = q.popleft()


        if visited[tx][ty] < visited[c[0]][c[1]]:

            # 잡아먹는 과정
            if len(xy_q) == 1:
                nx, ny = xy_q.popleft()
                result += visited[nx][ny] - 1
                arr[nx][ny] = 0

                size_arr[size][1] += 1
                if size_arr[size][1] == size_arr[size][0]:
                    size +=1

                q.clear()
                q.append([nx, ny])
                visited = [[0] * N for _ in range(N)]
                visited[nx][ny] = 1
                tx, ty = nx, ny
            elif len(xy_q) > 1:
                for i in range(N):
                    for j in range(N):
                        if [i, j] in xy_q:
                            nx, ny = i, j
                            xy_q.clear()
                            
                result += visited[nx][ny] - 1
                arr[nx][ny] = 0

                size_arr[size][1] += 1
                if size_arr[size][1] == size_arr[size][0]:
                    size +=1

                q.clear()
                q.append([nx, ny])
                visited = [[0] * N for _ in range(N)]
                visited[nx][ny] = 1
                tx, ty = nx, ny
            
            # 못잡아먹고 이동
            else:
                tx, ty = c[0], c[1]
                for i in range(4):
                    nx = c[0] + dx[i]
                    ny = c[1] + dy[i]

                    
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] <= size and not visited[nx][ny]:
                        q.append([nx, ny])
                        visited[nx][ny] = visited[c[0]][c[1]] + 1
                        if 0 < arr[nx][ny] < size:
                            xy_q.append([nx, ny])
        else:
            for i in range(4):
                nx = c[0] + dx[i]
                ny = c[1] + dy[i]

                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] <= size and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[c[0]][c[1]] + 1
                    if 0 < arr[nx][ny] < size:
                        xy_q.append([nx, ny])
            
            
# main
N = int(sys.stdin.readline())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
size = 2
size_arr = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [1000, 0]
]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x, y = i, j
            arr[x][y] = 0
BFS(x, y)
print(result)