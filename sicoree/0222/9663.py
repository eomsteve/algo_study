# 9663 / N-Queen
# https://www.acmicpc.net/problem/9663

def n_queen(x):
    global cnt
    if x == N:
        cnt += 1
    else:
        for i in range(N):
            row[x] = i
            for j in range(x):
                if row[x] == row[j] or row[x] - row[j] == x - j or row[x] - row[j] == j - x:
                    break
            else:
                n_queen(x + 1)

N = int(input())

cnt = 0
row = [0] * N

n_queen(0)
print(cnt)

# pypy3으로만 되고 python으로는 시간초과만 뜹니다