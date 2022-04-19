# https://www.acmicpc.net/problem/21608
# 상어 초등학교

def s_confirm(student):
    satisfaction = 0
    for i in range(N):
        for j in range(N):
            if c_map[i][j] == student[0]:
                for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        nr, nc = i+d[0], j+d[1]
                        if 0 <= nr < N and 0 <= nc < N:
                            if c_map[nr][nc] in student:
                                satisfaction += 1
                return satisfaction


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N*N)]
# 학생들을 놓을 위치
c_map = [[0]*N for _ in range(N)]
for student in arr:
    max_student = (0, 0)
    flg = (0, 0, 1)
    s_loc = (-1, -1)
    for i in range(N):
        for j in range(N):
            if c_map[i][j]:
                continue
            like_s = zero_s = 0
            for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr, nc = i+d[0], j+d[1]
                if 0 <= nr < N and 0 <= nc < N:
                    if c_map[nr][nc] in student:
                        like_s += 1
                    elif not c_map[nr][nc]:
                        zero_s += 1
            # 위치값 정의하기
            if max_student[0] <= like_s:
                if max_student[0] < like_s:
                    s_loc = (i, j)
                    max_student = (like_s, zero_s)
                elif max_student[1] < zero_s:
                    s_loc = (i, j)
                    max_student = (like_s, zero_s)
                elif like_s == 0 and zero_s == 0 and flg[2]:
                    flg = (i, j, 0)
    if max_student == (0, 0):
        s_loc = flg[:2]
    c_map[s_loc[0]][s_loc[1]] = student[0]
sum_s = 0
for student in arr:
    # 인접 학생 수 판별 함수
    num = s_confirm(student)
    if num == 0:
        sum_s += 0
    elif num == 1:
        sum_s += 1
    elif num == 2:
        sum_s += 10
    elif num == 3:
        sum_s += 100
    else:
        sum_s += 1000
print(sum_s)
