# 10026. 적록색약

# N = int(input())  # 전체 크기
#
# board = [list(input()) for _ in range(N)]
#
# visited = [[0]*N for _ in range(N)]
# color3_cnt = 0
# color2_cnt = 0
#
# dr = [0, 1, 0, -1]  # 우하좌상
# dc = [1, 0, -1, 0]
#
# def sol(r, c):  # dfs방식 이용
#     visited[r][c] = 1
#     cc = board[r][c]  # 현재 색깔 current color
#
#     for d in range(4):
#         nr, nc = r + dr[d], c + dc[d]
#         if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] == cc:
#             sol(nr, nc)
#
# # 3가지 색 구분
# for r in range(N):
#     for c in range(N):
#         if not visited[r][c]:
#             sol(r, c)
#             color3_cnt += 1
#
# # print(color3_cnt, end=' ')
# visited = [[0]*N for _ in range(N)]  # visited 초기화
#
# # 2가지 색 구분
# for r in range(N):
#     for c in range(N):
#         if board[r][c] == 'G':  # Green을  Red로 교체
#             board[r][c] = 'R'
#
# for r in range(N):
#     for c in range(N):
#         if not visited[r][c]:
#             sol(r, c)
#             color2_cnt += 1
#
# print(color3_cnt, color2_cnt)


'''
문제 접근 방식 : dfs 방식으로 문제 풀이

어려웠던점: 런타임 에러 (RecursionError)

설명이 필요한점: 
'''

from collections import deque

N = int(input())  # 전체 크기

board = [list(input()) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
queue = deque()
dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

def sol(r, c):  # bfs queue 사용
    queue.append([r, c])
    visited[r][c] = cnt
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] == board[r][c]:
                queue.append([nr, nc])
                visited[nr][nc] = 1

# 3가지 색 구분
cnt = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            sol(r, c)
            cnt += 1

print(cnt, end=' ')

# 2가지 색 구분
visited = [[0]*N for _ in range(N)]  # visited 초기화
cnt = 0  # cnt 초기화
for r in range(N):
    for c in range(N):
        if board[r][c] == 'G':  # Green을  Red로 교체
            board[r][c] = 'R'

for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            sol(r, c)
            cnt += 1

print(cnt)
'''
문제 접근 방식 : bfs queue방식으로 문제 풀이

어려웠던점:

설명이 필요한점: 
'''
