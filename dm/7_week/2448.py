# https://www.acmicpc.net/problem/2448
# 별 찍기 - 11


def star(idx):
    if idx <= 3:
        for i in range(idx):
            star_space[i][N-1-i:N+i] = [1]*i+[(i+1) % 2]+ [1]*i
        return
    star(idx//2)
    pt = idx//2
    for i in range(pt, idx):
        star_space[i][N-pt*2:N-1] = star_space[i-pt][N-pt:N+pt-1]
        star_space[i][N:N+pt*2-1] = star_space[i-pt][N-pt:N+pt-1]



N = int(input())
star_space = [[0 for _ in range(2*N-1)] for _ in range(N)]
star(N)
for a in star_space:
    print(''.join(list(map(lambda x: '*' if x else ' ', a))))
