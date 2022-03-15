# 1149 / RGB거리
# https://www.acmicpc.net/problem/1149

N = int(input())
# 0 = R, 1 = G, 2 = B
arr = [list(map(int, input().split())) for _ in range(N)]

y = 0

sum_arr = 0

for i in range(1, len(arr)):
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

print(min(arr[N - 1][0], arr[N - 1][1], arr[N - 1][2]))

# 접근 방법
# i번째 집을 R, G, B로 칠했을때 각 상황에 대하여 최솟값을 계속 초기화
# 그 후 i + 1집도 반복후 마지막에 도달한 값중 최소값을 프린트