# 1799 / 비숍
# https://www.acmicpc.net/problem/1799

# 인덱스, 비숍갯수, visited
def DFS(n, cnt, v):
    global result
    if n > (N - 1) * 2:
        if result < cnt:
            result = cnt
            return
    else:
        if n < N:
            for i in range(n + 1):
                if arr[i][n - i] == 1 and not v[n - (2 * i)]:
                    v[n - (2 * i)] = 1
                    DFS(n + 1, cnt + 1, v)
                    v[n - (2 * i)] = 0
        elif n >= N:
            for i in range(n - N + 1, N):
                if arr[i][n - i] == 1 and not v[n - (2 * i)]:
                    v[n - (2 * i)] = 1
                    DFS(n + 1, cnt + 1, v)
                    v[n - (2 * i)] = 0
        DFS(n + 1, cnt, v)
        return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# [차이 0, 차이 1, 차이 2, 차이 3, ... , 차이 -3, 차이 -2, 차이 -1]
visited = [0] * (N * 2)

result = 0
DFS(0, 0, visited)

print(result)

# 대각선 좌표들의 규칙성을 이용