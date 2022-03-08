# https://www.acmicpc.net/problem/10814
# 나이순 정렬


def quick_sort(a):
    if len(a) < 2:
        return a
    pivot = a[len(a) // 2][0]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in a:
        if int(num[0]) < int(pivot):
            lesser_arr.append(num)
        elif int(num[0]) > int(pivot):
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


N = int(input())
a_n_arr = []
for _ in range(N):
    a_n_arr.append(list(input().split()))

a_n_arr = quick_sort(a_n_arr)

for arr in a_n_arr:
    print(*arr)



'''
문제 접근 방식
- 퀵정렬을 통해 정렬하는 식으로 풀이

어려웠던 점
bubble_sort: time over
selection_sort: 입력받은 순 나열 불가
나이로 정렬을 하는데 입력에 문자가 있어 입력을 문자로 받아야함, 비교를 위해 나중에 나이를 int로 바꿔줘야함.

설명이 필요한점

'''