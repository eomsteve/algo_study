# https://www.acmicpc.net/problem/4690
# 완전 세제곱


per_lst = [i**3 for i in range(101)]

for a in range(2, 101):
    for b in range(2, a):
        for c in range(b, a):
            for d in range(c, a):
                if per_lst[a] == per_lst[b] + per_lst[c] + per_lst[d]:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')



'''
문제 접근 방식
- 완전 탐색 방식을 이용

어려웠던 점

설명이 필요한점

'''