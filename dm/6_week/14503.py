# https://www.acmicpc.net/problem/14503
# 로봇 청소기


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
v = [[0]*M for _ in range(N)]
cnt = 1
while True:
    # 1. 현재 위치를 청소합니다.
    v[r][c] = 1
    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색합니다.
    for cd in range(d-1, d-5, -1):
        cd %= 4
        nr = r+dir[cd][0]
        nc = c+dir[cd][1]
        if 0 <= nr < N and 0 <= nc < M:
            # 2-a, 2-b
            if not v[nr][nc] and not arr[nr][nc]:
                d = cd
                r, c = nr, nc
                cnt += 1
                break
    # 2-c
    else:
        r, c = r-dir[d][0], c-dir[d][1]
        # 2-d
        if not (0 <= r < N and 0 <= c < M) or arr[r][c]:
            break
print(cnt)
