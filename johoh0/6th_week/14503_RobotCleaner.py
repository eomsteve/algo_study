# 백준 14503 로봇청소기

dr = [-1, 0, 1, 0]  # 0: 북, 1: 동, 2: 남, 3: 서
dc = [0, 1, 0, -1]

def sol(r, c, d):
    global cnt
    if not board[r][c]:  # 청소 안된 구역 청소 후 cnt += 1
        board[r][c] = 2  # 청소구역은 벽이 아니며 돌아갈 수 있으니 1과 0이 아닌 숫자 구별
        cnt += 1

    for _ in range(4):  # 왼쪽방향부터 보게만들기
        temp_d = (d+3) % 4
        nr, nc = r + dr[temp_d], c + dc[temp_d]
        if not board[nr][nc]:  # 갈려는 방향이 청소를 안했을 경우
            sol(nr, nc, temp_d)  # 재귀를 사용하여 그 방향으로 청소시키기
            return
        d = temp_d  # 현재 보는 방향을 저장하여 다음 반복문 때 사용

    # 청소를 모든 방향이 끝마친 경우 뒷 방향으로 돌아가게 만들기
    back_d = (d + 2) % 4
    br, bc = r + dr[back_d], c + dc[back_d]
    if board[br][bc] == 1:  # 벽인 경우 리턴
        return
    else:  # 아닌 경우 청소하기 위해 재귀
        sol(br, bc, d)

N, M = map(int, input().split())  # N: 세로 크기, M: 가로 크기
sr, sc, d = map(int, input().split())  # sr, sc: 시작 위치, 첫 방향
board = [list(map(int, input().split())) for _ in range(N)]  # 지도 입력

cnt = 0
sol(sr, sc, d)
print(cnt)

'''
문제 접근 방식 : dfs

어려웠던점: 문제 이해가 조금 어려움? 헷갈림?

설명이 필요한점: 
'''