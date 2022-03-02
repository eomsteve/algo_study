# 9663 N-Queen
N = int(input())
col_check = [0] * N
dia1_check = [0]*(N*2-1)  # i+j, 대각선 좌상 -> 우하
dia2_check = [0]*(N*2-1)  # i-j+N-1, 대각선 우상 -> 좌하
cnt = 0
def N_Queen(idx):
    global cnt
    if idx == N:  # 모든 행에 퀸을 다 놓음!
        # 정답을 찾음!
        cnt += 1
        return
    # 퀸을 놓고 나서는 다음 행에 퀸 놓으러 가기
    # 모든 열에 퀸을 놓아보면 됨
    for i in range(N):
        # idx행 i열에 퀸 놓기 >> 다른 퀸의 영향을 받지 않으면 놓기
        if not col_check[i] and not dia1_check[idx+i] and not dia2_check[idx-i+N-1]:
            # arr[idx][i] = 1  # 퀸 놓기
            col_check[i] += 1
            dia1_check[idx + i] += 1
            dia2_check[idx - i + N - 1] += 1
            N_Queen(idx+1)
            # arr[idx][i]= 0  # 퀸 빼기, 영향 미치는 칸 표시 지우기
            col_check[i] -= 1
            dia1_check[idx + i] -= 1
            dia2_check[idx - i + N - 1] -= 1

N_Queen(0)
print(cnt)

'''
문제 접근 방식 : 수업 때 배운 N-Queen을 참고하여
dfs 개념 복습 겸 문제풀이하였습니다.

어려웠던점:

설명이 필요한점: 
'''