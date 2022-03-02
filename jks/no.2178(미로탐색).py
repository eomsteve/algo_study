N, M = map(int, input().split())
arr = [list(map(int, input().rstrip('\r'))) for _ in range(N)]
r, c = 0, 0
stack = [[r, c]]
visited = [[1] * M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
n = 1
n_min = 1000
while stack:
    print(n)
    vr, vc = stack[-1]
    if vr == N-1 and vc == M-1:
        if n < n_min:
            n_min = n
            n = 1
    else:
        visited[vr][vc] = 0
        for d in range(4):
            nr = vr + dr[d]
            nc = vc + dc[d]
            if 0 <= nr <= N-1 and 0 <= nc <= M-1 and arr[nr][nc] == 1 and visited[nr][nc] == 1:
                stack.append([nr, nc])
                n += 1
                break
        else:
            stack.pop()
            n -= 1
else:
    print(n_min)