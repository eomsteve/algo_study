N, M = map(int, input().split())
tree = list(map(int, input().split()))
h = max(tree)
n = 0
while True:
    for i in range(N):
        if tree[i] >= h:
            n += 1
    if n > M:
        print(h)
        break
    else:
        h -= 1
'''
문제접근방식 : 정렬해서 풀어보기

어려웠던점: 시간 초과ㅠㅠ

설명이 필요한점?
'''