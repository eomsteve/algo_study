# https://www.acmicpc.net/problem/2798
# 블랙잭


N, M = map(int, input().split())
arr = list(map(int, input().split()))


max_val = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
                sum_val = arr[i] + arr[j] + arr[k]
                if max_val < sum_val <= M:
                    max_val = sum_val
print(max_val)



'''
문제 접근 방식
- N개중 3장을 뽑아 더한값이 M을 넘지 않는다. arr값에서 3장을 선택해 더한값이 M을 넘지 않으면 max_val에 저장하고 최댓값을 찾는다.

어려웠던 점

설명이 필요한점

'''