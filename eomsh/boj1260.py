from collections import deque

N, M, V = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)


#  인접 행렬 만들기
def make_adj(v, edge_arr):
    arr = [[0] * (v+1) for _ in range(v+1)]
    for i in edge_arr:
        r, c = i[0], i[1]
        arr[r][c] = arr[c][r] = 1
    return arr


def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in range(1, N + 1):
        if visited_dfs[i] == 0 and adj[v][i] == 1:
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)
    visited_bfs[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if visited_bfs[i] == 0 and adj[v][i] == 1:
                q.append(i)
                visited_bfs[i] = 1


adj = make_adj(N, edges)

# print(adj)
dfs(V)
print()
bfs(V)
