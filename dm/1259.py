# https://www.acmicpc.net/problem/1259
# 팰린드롬수


while True:
    n = input()

    if n == '0':
        break

    print('yes' if n == n[::-1] else 'no')



'''
문제 접근 방식
- 파이썬은 [::-1]인덱싱이 있어 팬린드롬수 이지만 문자열로 접근해서 풀어봄

어려웠던 점

설명이 필요한점

'''