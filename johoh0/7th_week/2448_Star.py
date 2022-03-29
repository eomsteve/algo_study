# 백준 2448 별 찍기 - 11
def star_tree(i, j, n):  # 가장 위의 센터부터 분배
    if n == 3:  # 하나의 크기가 3일 때 크기 3의 별 모양을 만들어준다.
        board[i][j] = '*'
        board[i + 1][j - 1] = '*'
        board[i + 1][j + 1] = '*'
        for idx in range(-2, 3):
            board[i+2][j+idx] = '*'
    else:
        n_half = n // 2
        star_tree(i, j, n_half)
        star_tree(i + n_half, j + n_half, n_half)
        star_tree(i + n_half, j - n_half, n_half)

N = int(input())
width = 2*N-1  # 제일 아래 칸의 크기로 구함
board = [[' '] * width for _ in range(N)]  # 빈 칸 사이 안띄우면 간격 표시 안되니까 띄우기

star_tree(0, width//2, N)
for i in range(len(board)):
    print(''.join(board[i]))
'''
문제 접근 방식 : 예제를 보고 규칙을 찾아보니 N이 커질수록 그 앞의 완성된 모양을 반복한다.

어려웠던점 :  접근 시간 오래 걸림...

설명이 필요한점 : 
'''