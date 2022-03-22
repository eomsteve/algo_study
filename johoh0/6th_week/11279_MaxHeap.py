# 백준 11279 최대 힙

heapcount = 0

def heap_push(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    current = heapcount
    parent = heapcount // 2

    while parent > 0 and heap[parent] < heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent
        parent = current // 2

def heap_pop():
    global heapcount
    result = heap[1]
    heap[1] = heap[heapcount]
    heap[heapcount] = 0
    heapcount -= 1
    parent = 1
    child = parent * 2
    if child + 1 <= heapcount:
        if heap[child+1] > heap[child]:
            child += 1

    while heap[child] > heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
        child = parent*2
        if child + 1 <= heapcount:
            if heap[child + 1] > heap[child]:
                child += 1
    return result

N = int(input())
heap = [0] * (N+1)
for _ in range(N):
    v = int(input())
    if v == 0:
        if len(heap) == 0 or (len(heap)>0 and heap[1] == 0):
            print(0)
        else:
            print(heap_pop())

    else:
        heap_push(v)


'''
문제 접근 방식 : 힙 정렬과 반복문

어려웠던점: 런타임 에러 (IndexError)

설명이 필요한점: 
'''