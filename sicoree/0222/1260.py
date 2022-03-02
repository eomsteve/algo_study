# 1260 / DFS(깊이) BFS(너비)
# https://www.acmicpc.net/problem/1260

from collections import deque

def dfs(v):
  visit_list2[v] = 1        
  print(v, end = " ")
  for i in range(1, N + 1):
    if visit_list2[i] == 0 and check[v][i] == 1:
      dfs(i)

def bfs(v):
  q = deque()
  q.append(v)       
  visit_list[v] = 1   
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, N + 1):
      if visit_list[i] == 0 and check[v][i] == 1:
        q.append(i)
        visit_list[i] = 1

N, M, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

check = [[0] * (N + 1) for _ in range(N + 1)]

for x, y in arr:
    check[x][y] = 1
    check[y][x] = 1

visit_list = [0] * (N + 1)
visit_list2 = [0] * (N + 1)

dfs(V)
print()
bfs(V)

# queue의 기능을 해주는 deque를 알게되었다 ( 선입선출 )