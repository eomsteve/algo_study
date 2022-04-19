# https://www.acmicpc.net/problem/16236
# 아기 상어

import sys
from collections import deque
input = sys.stdin.readline


def bfs(shark):
    # 물고기를 다먹을 때 까지 반복
    queue = deque()
    while True:
        sr, sc, size, feed, t = shark
        queue.append((sr, sc))
        v = [[0]*N for _ in range(N)]
        v[sr][sc] = 1
        min_t = 500
        while queue:
            s = queue.popleft()
            for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr, nc = s[0]+d[0], s[1]+d[1]
                if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and arr[nr][nc] <= size:
                    v[nr][nc] = v[s[0]][s[1]] + 1
                    if 0 < arr[nr][nc] < size and min_t > v[nr][nc]:
                        min_t = v[nr][nc]
                    queue.append((nr, nc))
        # 최소거리 물고기를 냠냠
        min_loc = fish_loc(v, min_t, size)
        # 거리가 갱신되지 않으면 다먹었다고 판단, 시간을 반환
        if min_t == 500:
            return t
        # 상어의 위치 이동 및 몸집 키우기
        arr[sr][sc] = 0
        arr[min_loc[0]][min_loc[1]] = 9
        feed += 1
        if size == feed:
            size += 1
            feed = 0
        t += min_t
        shark = (min_loc[0], min_loc[1], size, feed, t-1)


def fish_loc(v, min_t, size):
            for i in range(N):
                for j in range(N):
                    if v[i][j] == min_t and 0 < arr[i][j] < size:
                        return i, j


def s_loc(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                # r, c, size, feed, time
                return i, j, 2, 0, 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = s_loc(arr)
print(bfs(shark))
