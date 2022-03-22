# https://www.acmicpc.net/problem/11279
# 최대 힙


import sys
input = sys.stdin.readline


def enh(n):
    global last
    last += 1
    if last >= len(heap):
        heap.append(n)
    else:
        heap[last] = n
    c = last
    p = c//2
    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2


def deh():
    global last
    if last == 0:
        return 0
    if last == 1:
        tmp = heap[1]
        heap[last] = 0
        return tmp
    else:
        tmp = heap[1]
        heap[1] = heap[last]
        heap[last] = 0
        last -= 1 if last else 0
        p = 1
        c = p*2
        while c <= last:
            if c+1 <= last and heap[c] < heap[c+1]:
                c += 1
            if heap[p] < heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
                p = c
                c = p*2
            else:
                break
        return tmp


N = int(input())
heap = [0]
last = 0
for _ in range(N):
    x = int(input())
    if x:
        enh(x)
    else:
        print(deh())
