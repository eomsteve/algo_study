from itertools import combinations
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])

# 치킨 리스트 중에 M개씩 뽑아서 비교해서 저장하고 최소값 찾자
# n = len(chicken)
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(chicken[j], end='')
#     print()

# 집 돌아가면서 치킨집과 거리 비교 해서 가장 가까운 거리를 result에 더하면 될 거 같은데
d_list = []
for c in combinations(chicken, M):
    result = 0
    for h in home:
        min_d = 999
        for i in range(M):
            distance = abs(c[i][0]-h[0])+abs(c[i][1]-h[1])
            if distance <= min_d:
                min_d = distance
        result += min_d
    d_list.append(result)
print(min(d_list))
