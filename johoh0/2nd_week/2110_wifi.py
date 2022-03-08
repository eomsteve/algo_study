# 2110 공유기
import sys
sys.stdin = open('wifi.txt', 'r')

N, C = map(int, input().split())    # 집의 개수: N, 공유기 빈칸 허용: C
arr = [int(input()) for _ in range(N)]    # 배열 입력

def bubble_sort(arr):   # 개선된 버블정렬
    n = len(arr)
    for a in range(n-1, 0, -1):
        change = False
        for j in range(a):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                change = True
        if not change:
            break
    return arr

bubble_sort(arr)  # 정렬
# arr.sort()
start = 1  # 시작점: 제일 가까운 거리
end = arr[-1] - arr[0]  # 끝점: 제일 먼 거리
result = 0

while start <= end:
    middle = (start + end) // 2
    check = arr[0]  # 배열의 가장 작은 수
    cnt = 1  # 1번은 설치
    for i in range(1, len(arr)):  # 8번 설치, 4번 설치
        if arr[i] >= check + middle:
            cnt += 1
            check = arr[i]

    if cnt >= C:    # 공유기 분배 끝
        start = middle + 1
        result = middle
    else:
        end = middle - 1

print(result)
'''
문제 접근 방식 : 주어진 배열을 정렬 후 이진 탐색 이용

어려웠던점: 거리 재는 거에 대한 개념?

설명이 필요한점: pypy로만 통과 python으로는 시간초과
'''