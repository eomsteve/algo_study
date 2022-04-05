# 백준 2636 치즈

# def sol(r, c, hour):
#     for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
#             v[r][c] = hour
#
# def after_cheese(hour):
#     global min_cnt
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 1:
#                 cnt += 1
#                 sol(i, j, hour)
#
#     if min_cnt > cnt and cnt > 0:
#         min_cnt = cnt
#
#     for i in range(N):
#         for j in range(M):
#             if v[i][j] == hour:
#                 board[i][j] = 0
#
#     if cnt:
#         return after_cheese(hour+1)
#     else:
#         return hour-1
#
#
# N, M = map(int, input().split())  # N: 행의 길이, M: 열의 길이
# board = [list(map(int, input().split())) for _ in range(N)]
# v = [[0]*M for _ in range(N)]
# min_cnt = 10000
#
# print(after_cheese(1))
# print(min_cnt)

'''
문제 접근 방식 : 가운데에도 녹는 줄 알고 잘못 작성...

어려웠던점 :

설명이 필요한점 : 
'''

def bfs():
    global min_cnt
    q = [(0, 0)]
    v = [[0] * M for _ in range(N)]
    v[0][0] = 1
    cnt = 0  # 치즈의 수
    while q:
        r, c = q.pop(0)

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
                if board[nr][nc] == 0:
                    # 공기인 부분에서만 q 반복 실해하게 하기
                    q.append((nr, nc))
                    v[nr][nc] = 1
                elif board[nr][nc] == 1:
                    # 가장 자리 부분 치즈만 카운트 하고 내부에 더 못들어가게 v = 1 처리
                    board[nr][nc] = 0
                    cnt += 1
                    v[nr][nc] = 1

    if cnt > 0 and min_cnt > cnt:
        # 치즈가 존재하고, 최소값보다 작을 때 최소값 갱신
        min_cnt = cnt

    return cnt

N, M = map(int, input().split())  # N: 행의 길이, M: 열의 길이
board = [list(map(int, input().split())) for _ in range(N)]
min_cnt = 0xffffff

hour = 0
while True:
    hour += 1
    cnt = bfs()  # 공기와 접촉한 테두리의 치즈 구하기
    if cnt == 0:
        break
    print(cnt)
print(hour-1)
print(min_cnt)

'''
문제 접근 방식 : bfs

어려웠던점 : bfs 내부의 조건 처리

설명이 필요한점 : 
'''