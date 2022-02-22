# # https://www.acmicpc.net/problem/2110
# # 공유기 설치


import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
# 집의 x좌표를 순서대로 정렬함
house.sort()
# house가 가질 수 있는 최소거리 min_d, 최대거리 max_d
# 그 갯수가 C라면 이때의 거리를 출력함
min_d = 1
max_d = house[N-1] - house[0]
result = 0
while min_d <= max_d:
    mid_d = (max_d + min_d) // 2
    # 처음 0에 공유기를 설치했다고 가정, 설치했으므로 cnt = 1
    now = house[0]
    cnt = 1
    # 다음 거리가 mid_d 이상 차이가 난다면 cnt를 올리고 현재 설치한 위치를 초기화 함.
    for i in range(1, N):
        if house[i] >= now + mid_d:
            cnt += 1
            now = house[i]
    # cnt 와 설치갯수가 같다면 반복문을 탈출
    # cnt == C를 하지 않는 이유? (cnt == C 인 최초의 값)cnt는 같을 수 있지만, 출력값이 두 공유기 사이의 최대 거리를 출력해야 하는데 최대거리가 아닐 수 있음.
    if cnt >= C:
        min_d = mid_d + 1
        result = mid_d
    else:   # cnt < C
        max_d = mid_d - 1
print(result)



'''
문제 접근 방식
- 이진탐색을 이용해 거리를 반씩 좁혀가며 간격을 출력함.

어려웠던 점
- 최소거리를 어떻게 잡아야 할 지 몰랐는데 이분탐색 알고리즘을 통해 거리를 가감하면서 접근
- import sys 미 사용시 시간초과

설명이 필요한점

'''