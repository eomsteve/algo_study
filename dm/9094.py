# https://www.acmicpc.net/problem/9094
# 수학적 호기심


import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    cnt = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            if (a*a+b*b+m) % (a*b) == 0:
                cnt += 1
    print(cnt)


'''
문제 접근 방식
- 분모를 분자로 나눈 나머지가 0 이면 정수이다.

어려웠던 점
- 시간초과가 계속 떠서 input을 sys로 받고, 제곱을 곱셈으로 바꾸고 a, b 범위를 최소화함.

설명이 필요한점

'''