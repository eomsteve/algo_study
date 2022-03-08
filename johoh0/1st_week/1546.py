# 1546번 평균

N = int(input())

lst = list(map(int, input().split()))
max_v = 0
for i in range(N):
    if max_v < lst[i]:
            max_v = lst[i]

sum_v = 0
for i in range(N):
    sum_v += lst[i] / max_v * 100

avg_v = sum_v / N
print(avg_v)

'''
문제접근방식 : 입력을 받고 반복문을 사용하여 최대값 찾은 후
100 / 최대값을 기존의 값에 더한 후 평균을 구해주었다.

어려웠던점:

설명이 필요한점?

'''