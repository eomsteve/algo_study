# https://www.acmicpc.net/problem/10773
# 제로


K = int(input())
arr = []
for _ in range(K):
    N = int(input())
    if N:
        arr.append(N)
    else:
        arr.pop()
sum_val = 0
for i in arr:
    sum_val += i
print(sum_val)



'''
문제 접근 방식
- 입력받은 값이 0이 아니면 리스트에 추가하고, 0이면 추가했던 값을 뺀다.

어려웠던 점

설명이 필요한점

'''