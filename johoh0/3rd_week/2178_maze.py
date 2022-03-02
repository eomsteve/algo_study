# 2178 미로 탐색
# 우 하 좌 상 방향
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
stack = [(0, 0)]  # 출발점 (0, 0) 추가한 초기 설정
visited[0][0] = 1
cnt = 1  # 첫 자리 1을 센 초기상태
while stack:
    cr, cc = stack[-1]  # 현재 위치 설정
    # 현재 위치가 N-1, M-1이면 통과
    if cr == N-1 and cc == M-1:
        print(cnt)
        break

    # 현재 위치에서 4방향 조사
    for d in range(4):  # 상하좌우 조사
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == '1' and not visited[nr][nc]:
            # 범위 넘어가지 않고 / 값이 '1'인 통로이며 / 방문하지 않은 곳
            stack.append((nr, nc))
            visited[nr][nc] = 1
            cnt += 1
            break
    else:
        stack.pop()
#         cnt -= 1

'''
문제 접근 방식 : stack의 dfs방식

어려웠던점: 경로는 찾는데, 최단 경로는 못찾는...

설명이 필요한점: 
'''








