# https://www.acmicpc.net/problem/1012
# 유기농 배추


# 파이썬 재귀함수를 사용할 경우 1000개가 한계이므로 setrecursionlimit를 이용해 재귀의 깊이를 늘려줘야함.
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(cr, cc):
    arr[cr][cc] = 0
    # 4방향 탐색
    for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr = cr + d[0]
        nc = cc + d[1]
        # 탐색한 부분이 1이리면, arr을 메꾸고 다음경로 탐색
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
            dfs(nr, nc)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    # 행렬 생성
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1
    # 배추가 심어져 있는 부분에 dfs를 사용
    cnt = 0
    for a in range(N):
        for b in range(M):
            if arr[a][b]:
                dfs(a, b)
                cnt +=1 
    print(cnt)
