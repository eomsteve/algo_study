# https://www.acmicpc.net/problem/3584
# 가장 가까운 공통 조상 다국어

import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    t_arr = [0]*(N+1)
    for i in range(N-1):
        p, c = map(int, input().split())
        t_arr[c] = p
    a, b = map(int, input().split())
    a_p = [a]
    while a:
        a_p.append(t_arr[a])
        a = t_arr[a]
    while b:
        if b in a_p:
            print(b)
            break
        b = t_arr[b]
