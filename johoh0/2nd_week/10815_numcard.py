# 10815번 숫자 카드
import sys
sys.stdin = open('numcard.txt', 'r')

# N = int(input())  # 카드의 개수
# card = list(map(int, input().split()))
# M = int(input())  # 확인 카드의 개수
# check = list(map(int, input().split()))
#
# # arr = [0] * M  # 카드 유무 확인 배열 초기화
# for m in range(M):
#     a = 0
#     for n in range(N):
#         if card[n] == check[m]:  # 요소의 숫자들 같으면 a=1 후 break
#             # arr[m] = 1
#             a = 1
#             break
#     print(a, end=' ')

# 이중 반복문 시간 초과

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

N = int(input())  # 카드의 개수
card = list(map(int, input().split()))
M = int(input())  # 확인 카드의 개수
check = list(map(int, input().split()))

# card.sort()
bubble_sort(card)

for m in range(M):
    start = 0
    end = N-1
    result = 0
    while start <= end:
        middle = (start + end) // 2
        if check[m] == card[middle]:
            result = 1
            break
        elif check[m] < card[middle]:
            end = middle - 1
        else:
            start = middle + 1

    print(result, end=' ')

# 이진 탐색 사용
# sort() OK bubble_sort 시간초과
'''
문제 접근 방식 : 자신의 카드를 정렬하여 확인해야하는 카드를 이진 탐색으로 구간을 좁히며 검사

어려웠던점: 이진 탐색으로 해결은 봤으나 sort() 사용

설명이 필요한점: 
'''