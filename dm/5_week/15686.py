# https://www.acmicpc.net/problem/15686
# 치킨 배달


def subset(n):
    global min_len
    if n == queue_len:
        s_v = sum(visitied)
        # 최대 치킨집의 갯수가 M개이므로 M이 넘으면 안됨
        if  s_v > M:
            return
        # 해당 집합 마다 도시키의 치킨 거리의 최솟값을 구함
        selected = [100]*home_len
        for i in range(queue_len):
            if visitied[i] == 1:
                for j in range(home_len):
                    selected[j] = min(selected[j], v[i][j])
        sum_val = sum(selected)
        # 모든 부분집합 중 최솟값을 찾음
        if min_len > sum_val:
            min_len = sum_val
        return
    # 부분집합을 재귀함수를 이용해 구함
    visitied[n] = 0
    subset(n+1)
    visitied[n] = 1
    subset(n+1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = []
home = []
# 치킨집(2)와 가정(1)의 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            queue.append((i, j))
        if arr[i][j] == 1:
            home.append((i, j))
home_len = len(home)
queue_len = len(queue)
v = [[0]*home_len for _ in range(queue_len)]
visitied = [0]*queue_len
# 거리값을 v 배렬에 저장함
for i in range(queue_len):
    for j in range(home_len):
        v[i][j] = abs(queue[i][0]-home[j][0]) + abs(queue[i][1]-home[j][1])
min_len = 10**6
loc=[]
subset(0)
print(min_len)
