def dfs(n):
    if n == M:
        for k in s:
            print(k, end=' ')
        print()
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            s.append(i + 1)
            dfs(n + 1)
            visited[i] = 0
            s.pop()


N, M = map(int, input().split())
visited = [0] * N
s = []
dfs(0)