def solution(line):
    stars = []
    N = len(line)

    for i in range(N):
        for j in range(i + 1, N):
            a1, b1, c1 = line[i]
            a2, b2, c2 = line[j]
            if a1 * b2 - a2 * b1 != 0:  # 분수의 분모는 0이 될 수 없음..
                x = (c2 * b1 - c1 * b2) / (a1 * b2 - a2 * b1)  # 공식이 아래에 있었군요... 노트에 필기하고 알아냈는데;; ㅠ
                y = (c2 * a1 - c1 * a2) / (b1 * a2 - b2 * a1)
                if x.is_integer() and y.is_integer():  # 정수확인 후 정수화 시켜주기
                    x, y = int(x), int(y)
                    if (x, y) not in stars:
                        stars.append((x, y))

    x_min, x_max = min(stars)[0], max(stars)[0]
    y_min, y_max = min(stars, key=lambda x: x[1])[1], max(stars, key=lambda x: x[1])[
        1]  # 그냥 min, max하면 첫 번째열에 붙어있는 두 번째 열의 값 반환, 그래서 두 번째열부터 구하는 식 알아두기

    board = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]  # "." 찍힌 배열 만들기

    for x, y in stars:  # 별 찍어야하는 좌표는 "*" 로 값 바꿔주기
        board[y_max - y][x - x_min] = "*"

    return [''.join(s) for s in board]

'''
문제 접근 방식 : 공식과 조건을 이용하여 별을 찍어야하는 정수로 된 지점을 구하고, 
                최댓값, 최솟값을 구해 전체 그림의 크기 구한 뒤, "."으로 채우고,
                별 위치에는 "*" 넣어주기 

어려웠던점 : y의 최소, 최대값을 구할 때, 일반적인 min, max로 구하기 힘듦

설명이 필요한점 : 
'''