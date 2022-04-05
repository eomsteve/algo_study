# https://www.acmicpc.net/problem/1987
# 알파벳


import sys
input = sys.stdin.readline


def bfs(r, c):
    queue = set()
    queue.add((r, c, arr[r][c]))
    max_val = 0
    while queue:
        s = queue.pop()
        max_val = max(max_val, len(s[2]))
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = s[0] + d[0]
            nc = s[1] + d[1]
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in s[2]:
                queue.add((nr, nc, s[2] + arr[nr][nc]))
    print(max_val)


R, C = map(int, input().split())
arr = [input() for _ in range(R)]
bfs(0, 0)
