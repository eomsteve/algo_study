# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기


def calculation(idx, cal):
    global max_v, min_v
    if idx == N-1:
        if max_v < cal:
            max_v = cal
        if min_v > cal:
            min_v = cal
        return
    for i in range(4):
        if o[i] > 0:
            o[i] -= 1
            save[idx] = i
            if i == 0:
                calculation(idx+1, cal + a[idx+1])
            elif i == 1:
                calculation(idx+1, cal - a[idx+1])
            elif i == 2:
                calculation(idx+1, cal * a[idx+1])
            else: # i == 3
                calculation(idx+1, -(abs(cal) // a[idx+1]) if cal < 0 else cal // a[idx+1])
            o[i] += 1
            save[idx] = -1

N = int(input())
a = list(map(int, input().split()))
# 덧셈, 뺼셈, 곱셈, 나눗셈
o = list(map(int, input().split()))
save = [-1]*(N-1)
max_v , min_v = -10**9, 10**9 
calculation(0, a[0])
print(max_v)
print(min_v)