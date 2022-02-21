# https://www.acmicpc.net/problem/2841
# 외계인의 기타 연주


import sys
input = sys.stdin.readline


N, P = map(int, input().split())
flet = [list(map(int, input().split())) for _ in range(N)]
# 기타의 줄의 갯수 = 6개
stack = [[0 for _ in range(300000)] for _ in range(6)]
cnt = 0
sp = [0]*6
for line, f in flet:
    line = line-1
    # stack[f[0]][-1] 보다 f[1]이 크다면 stack에 쌓음
    if stack[line][sp[line]] < f:
        sp[line] += 1
        stack[line][sp[line]] = f
        cnt += 1
    # 작다면, f[1]보다 큰 값을 모두 제거
    elif stack[line][sp[line]] > f and stack[line][sp[line]] != f:
        while stack[line][sp[line]] > f:
            stack[line][sp[line]] = 0
            sp[line] -= 1
            cnt += 1
        # 그리고 stack의 끝값과 f[1]이 다르면 stack에 쌓음
        if stack[line][sp[line]] != f:
            sp[line] += 1
            stack[line][sp[line]] = f
            cnt += 1
    # 같으면, pass
print(cnt)



'''
문제 접근 방식
- 스택 구조를 이용해 문제가 원하는 답을 얻어보자.

어려웠던 점
- stack구조를 사용하여 append, pop 함수를 사용 했었는데 시간초과가 나옴

설명이 필요한점

'''