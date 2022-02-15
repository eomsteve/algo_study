# https://www.acmicpc.net/status?group_id=13727
# 도비의 영어 공부


while True:
    arr = input().lower()
    a = arr[0]
    sum_val = 0
    for i in range(2, len(arr)):
        if a == arr[i]:
                sum_val += 1
    if a != '#':
        print(a, sum_val)
    else:
        break



'''
문제 접근 방식
- 문자열로 접근

어려웠던 점

설명이 필요한점

'''