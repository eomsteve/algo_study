# https://www.acmicpc.net/problem/15829
# Hashing


L = int(input())
voca = list(map(ord, input()))

M = 1234567891
hash_val = 0
for i in range(len(voca)):
    hash_val += (voca[i]-96)*31**(i)
print(hash_val % M)



'''
문제 접근 방식
- 문제 수식을 그대로 구현

어려웠던 점
- 문제 수식을 잘 읽어보자.

설명이 필요한점

'''