# https://www.acmicpc.net/problem/7569
# 토마토


import sys
from collections import deque

input = sys.stdin.readline
# 최소 몇일 걸리는지 = bfs
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# queue 행렬 생성
queue = deque()
# 익은 토마토 찾기
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                queue.append((k, i, j))
# bfs
while queue:
    z, x, y = queue.popleft()
    for d in [[0, 0, 1], [0, 1, 0], [0, 0, -1], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]:
        ch = z + d[0]
        cr = x + d[1]
        cc = y + d[2]
        if 0 <= ch < H and 0 <= cr < N and 0 <= cc < M and not arr[ch][cr][cc]:
            arr[ch][cr][cc] = arr[z][x][y] + 1
            queue.append((ch, cr, cc))

# 결과 출력
def result():
    max_val = -1
    for k in range(H):
        for i in range(N):
            for j in range(M):
                # 토마토가 모두 익지 못한다면 -1 출력
                if arr[k][i][j] == 0:
                    return -1
                if max_val < arr[k][i][j]:
                    max_val = arr[k][i][j]
    # 토마토가 모두익는 최소일 또는 모두 익은상태일떄 0 출력
    return max_val-1

print(result())

'''
시간초과 문제
- 처음 pop(0)를 사용했었는데 시간초과가 나와 (x%10000)을 사용하는 인덱스 형태로 queue를 바꿔봤는데 코드를 잘못짠건지 인덱싱 에러와 코드를 바꿔봐도 시간초과가 떠서 queue를 deque로 바꿔 사용.
# pop(0)가 시간을 많이 잡아먹는것 같다.
'''