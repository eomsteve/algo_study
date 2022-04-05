# 백준 1987 알파벳

def sol():
    global res

    q = [(0, 0)]
    v = [[0]*C for _ in range(R)]
    used = [board[0][0]]
    v[0][0] = 1
    cnt = 1
    while q:
        r, c = q.pop(0)
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not v[nr][nc]:
                if board[nr][nc] not in used:
                    used.append(board[nr][nc])
                    cnt += 1
                    q.append((nr, nc))
                    v[nr][nc] = 1

    if res < cnt:
        res = cnt

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

res = 0
sol()
print(res)

'''
문제 접근 방식 : bfs

어려웠던점 : 케이스가 많아질 경우 답이 틀려짐

설명이 필요한점 : fail 
'''