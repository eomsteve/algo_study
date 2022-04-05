# https://www.acmicpc.net/problem/1799
# 비숍


import sys
input = sys.stdin.readline


def bk(idx, cnt):
    global max_cnt
    if 2*N-1-idx + cnt <= max_cnt:
        return
    if idx == 2*N-1:
        max_cnt = max(max_cnt, cnt)
        return
    if idx < N:
        for i in range(idx+1):
            if arr[idx-i][i] and not v1[idx] and not v2[i-(idx-i)+(N-1)]:
                v1[idx] = 1
                v2[i-(idx-i)+(N-1)] = 1
                bk(idx+1, cnt+1)
                v1[idx] = 0
                v2[i-(idx-i)+(N-1)] = 0
        else:
            bk(idx+1, cnt)
    else:
        for i in range((2*N-1)-idx):
            if arr[idx-(N-1)+i][(N-1)-i] and not v1[idx] and not v2[2*((N-1)-i)-idx+(N-1)]:
                v1[idx] = 1
                v2[2*((N-1)-i)-idx+(N-1)] = 1
                bk(idx+1, cnt+1)
                v1[idx] = 0
                v2[2*((N-1)-i)-idx+(N-1)] = 0
        else:
            bk(idx+1, cnt)

    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v1 = [0]*(2*N-1)  # r+c
v2 = [0]*(2*N-1)  # c-r+(N-1)
flg = [0]*(2*N-1)
max_cnt = 0
bk(0, 0)
print(max_cnt)
