# 백준 14888 연산자 끼워넣기

def sol(i, arr):  # dfs
    global max_v, min_v, add, sub, mtp, div
    if i == N:
        max_v = max(max_v, arr)
        min_v = min(min_v, arr)
    else:
        if add > 0:
            add -= 1
            sol(i+1, arr + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            sol(i + 1, arr - nums[i])
            sub += 1
        if mtp > 0:
            mtp -= 1
            sol(i+1, arr * nums[i])
            mtp += 1
        if div > 0:
            div -= 1
            sol(i+1, int(arr / nums[i]))  # 나누기 주의! 정수부분만 취한다.
            div += 1

N = int(input())  # N: 숫자의 개수
nums = list(map(int, input().split()))
add, sub, mtp, div = map(int, input().split())  # 사칙연산 개수 저장

min_v = 1 * (10**9)
max_v = -1 * (10**9)

sol(1, nums[0])

print(max_v)
print(min_v)
'''
문제 접근 방식 : dfs

어려웠던점:

설명이 필요한점: 
'''