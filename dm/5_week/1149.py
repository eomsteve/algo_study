# https://www.acmicpc.net/problem/1149
# RGB거리


import sys
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# R, G, B 각 위치마다 이전 자기자신의 값을 제외한 최솟값을 더해감
for i in range(1, N):
    arr[i][0] += min(arr[i-1][1] ,arr[i-1][2])
    arr[i][1] += min(arr[i-1][0] ,arr[i-1][2])
    arr[i][2] += min(arr[i-1][1] ,arr[i-1][0])
print(min(arr[N-1]))