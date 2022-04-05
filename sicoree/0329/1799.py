# 1799 / 비숍
# https://www.acmicpc.net/problem/1799

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
                    DFS(n + 2, cnt + 1, v)
                    v[n - (2 * i)] = 0
        elif n >= N:
            for i in range(n - N + 1, N):
                if arr[i][n - i] == 1 and not v[n - (2 * i)]:
                    v[n - (2 * i)] = 1
                    DFS(n + 2, cnt + 1, v)
                    v[n - (2 * i)] = 0
        DFS(n + 2, cnt, v)
        return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * (N * 2)

result = 0
DFS(0, 0, visited)
result_b = result

result = 0
DFS(1, 0, visited)
result_b += result

print(result_b)

# 대각선 좌표들의 규칙성을 이용