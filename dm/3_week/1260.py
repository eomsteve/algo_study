# https://www.acmicpc.net/problem/1260
# DFS와 BFS


# dfs 재귀
def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, N+1):
        if adj[v][i] and not visited[i]:
            dfs(i)


N, M, V = map(int, input().split())
# 인접행렬 생성
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    # 양방향 간선
    adj[a][b] = 1
    adj[b][a] = 1
# 1. dfs
# 방문행렬 생성
visited = [0] * (N+1)
# stack 행렬 생성
stack = []
# V부터 방문
stack.append(V)
visited[V] = 1
path = [V]
# dfs
# 스택이 비어있으면 반복문 정지
while stack:
    dot = stack[-1]
    # adj[v][i]를 확인 해 1이고, 방문을 안했다면 이동
    for i in range(1, N+1):
        if adj[dot][i] and not visited[i]:
            stack.append(i)
            path.append(i)
            visited[i] = 1
            break
    # 길이 없다면 pop을 하고 재 탐색
    else:
        stack.pop()
print(*path)
# 2. bfs
# 방문행렬 생성
visited = [0] * (N+1)
visited[V] = 1
# queue 행렬 생성
queue = [V]
while queue:
    front = queue.pop(0)
    print(front, end=' ')
    for i in range(1, N+1):
        if adj[front][i] and not visited[i]:
            queue.append(i)
            visited[i] = visited[front]+1