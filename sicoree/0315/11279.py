# 11279 / 최대 힙
# https://www.acmicpc.net/problem/11279

import sys

def enq(x):
    arr.append(x)
    p = len(arr) - 1
    c = p // 2
    while p >= 2 and arr[p] > arr[c]:
        if arr[p] > arr[c]:
            arr[p], arr[c] = arr[c], arr[p]
            p = c
            c = p // 2

def deq():
    result = arr[1]

    val = arr.pop()

    p = 1
    c = p * 2
    while c <= len(arr) - 1:        
        if c < len(arr) - 1 and arr[c] < arr[c + 1]:
            c += 1

        if arr[c] <= val:
            break

        arr[p] = arr[c]

        p = c
        c = p * 2
    
    if len(arr) - 1 != 0:
        arr[p] = val
    return result

N = int(sys.stdin.readline())
arr = [0]

for n in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(arr) == 1:
            print(0)
        else:
            print(deq())
    elif x != 0:
        enq(x)