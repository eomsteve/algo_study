# 1074. Z

N, r, c = map(int, input().split())

cnt = 0

# 계속하여 4분할하는
def sol(size, nr, nc):  # 4분할하는 크기, 최상단좌측인자들을 요소로 받음
    global cnt
    if nr == r and nc == c:
        print(int(cnt))  # float 값 나올 수 있어서 int처리
        return

    if size == 1:
        cnt += 1
        return

    if not nr <= r < nr + size and not nc <= c < nc + size:
        cnt += size ** 2
        return
    # 4분할 시켜 재귀
    sol(size / 2, nr, nc)  # 좌상단
    sol(size / 2, nr, nc + size / 2)  # 우상단
    sol(size / 2, nr + size / 2, nc)  # 좌하단
    sol(size / 2, nr + size / 2, nc + size / 2)  # 우하단

size = 2 ** N  # 한 변의 크기: 2 ** N
sol(size, 0, 0)

'''
문제 접근 방식 : dfs방식으로 

어려웠던점:

설명이 필요한점: 
'''

