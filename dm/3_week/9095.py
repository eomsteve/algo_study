# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기


def sum_method(idx, sum_val):
    global cnt
    # 합이 N과 같으면 다음 가지로 넘어감
    if sum_val == N:
        cnt += 1
        return
    # 또는 idx가 N까지 갔다면 return
    if idx == N:
        return
    # 1, 2, 3 을 사용
    for i in range(1, 4):
        sum_method(idx+1, sum_val+i)


for _ in range(int(input())):
    N = int(input())
    cnt = 0
    sum_method(0, 0)
    print(cnt)