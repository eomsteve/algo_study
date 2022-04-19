# 백준 19236 청소년 상어

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(r, c , dir, sum_v):
    global res, board, sh

    board_save = [[[]]*4 for _ in range(4)]  # 배열 복사
    for i in range(4):
        for j in range(4):
            board_save[i][j] = board[i][j][:]

    move()  # 물고기 움직임 함수 실행

    if res < sum_v:
        res = sum_v

    for i in range(1, 4):
        nr, nc = r + dr[dir]*i, c + dc[dir]*i

        if not 0 <= nr < 4 or not 0 <= nc < 4:
            break  # 범위 바깥은 스킵
        if board[nr][nc][0] == 0:
            continue  # 물고기 없으면 스킵

        tmp = board[nr][nc][:]  # 물고기 번호, 방향 임시 정보
        board[r][c][0] = 0
        board[nr][nc][0] = -1
        dfs(nr, nc, board[nr][nc][1], sum_v + tmp[0])
        # 되돌리기
        board[r][c][0] = -1
        board[nr][nc][0] = tmp[0]

    for i in range(4):
        for j in range(4):
            board[i][j] = board_save[i][j][:]

def move():
    for f in range(1, 17):  # 물고기 작은 번호 순부터 이동
        check = False  # 움직임 체크
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == f and not check:
                    for d in range(8):
                        dir = board[i][j][1]
                        nd = (dir + d) % 8  # 새로운 방향 조정
                        ni, nj = i + dr[nd], j + dc[nd]
                        if not 0 <= ni < 4 or not 0 <= nj < 4:
                            continue  # 범위 밖이면 스킵
                        if board[ni][nj] == -1:
                            continue  # 상어가 있으면 스킵
                        board[i][j][1] = nd
                        board[ni][nj], board[i][j] = board[i][j], board[ni][nj]
                        check = True  # 움직였으므로 체크
                        break

board = [[[]]*4 for _ in range(4)]

for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = [lst[j*2], lst[j*2+1]-1]  # 배열에 정보끼리 입력

res = 0
sh = board[0][0][:]  # 상어
board[0][0][0] = -1  # 상어 위치 초기값 변경해주기
dfs(0, 0, sh[1], sh[0])

print(res)

'''
문제 접근 방식 : dfs를 사용한 완전탐색

어려웠던점 : 1, 2 case 정답 보고 제출했으나 틀림, 3 X, 4 O 

설명이 필요한점 : 
'''