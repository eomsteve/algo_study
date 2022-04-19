# 1759 / 암호 만들기
# https://www.acmicpc.net/problem/1759

import sys

def solve(idx, selected, cnt):
    if cnt == L:
        comb = []
        for idx in range(C):
            if selected[idx] == 1:
                comb.append(arr[idx])
        a_cnt = b_cnt = 0

        for char in comb:
            if char in arr_a:
                a_cnt += 1
            else:
                b_cnt += 1
        if a_cnt > 0 and b_cnt > 1:
            result.append("".join(comb))
        return

    if idx == C:
        return
    else:
        selected[idx] = 1
        solve(idx + 1, selected, cnt + 1)
        selected[idx] = 0
        solve(idx + 1, selected, cnt)

L, C = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
result = []
arr.sort()
arr_a = ['a', 'e', 'i', 'o', 'u']

solve(0, [0] * C, 0)

for row in result:
    print(row)