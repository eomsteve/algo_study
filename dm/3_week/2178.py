# https://www.acmicpc.net/problem/2178
# 미로 탐색


# 최단거리 = bfs
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# 방문 행렬 만들기
v = [[0 for _ in range(M)] for _ in range(N)]
queue = [(0, 0)]
v[0][0] = 1
while queue:
    front = queue.pop(0)
    # 4방향 탐색
    for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr = front[0] + d[0]
        nc = front[1] + d[1]
        # 해당 조건일 경우 길이 있다고 판단, 출발!
        while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not v[nr][nc]:
            queue.append((nr, nc))
            v[nr][nc] = v[front[0]][front[1]] + 1
print(v[N-1][M-1])
