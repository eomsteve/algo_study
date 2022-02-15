# https://www.acmicpc.net/problem/20410
# 추첨상 사수 대작전! (Easy)


def rand_easy(m, seed, x1, x2):
    for a in range(m):
        for c in range(m):
            if x1 == (a*seed + c) % m:
                if x2 == (a*x1 + c) % m:
                    print(a, c)
                    return

m, seed, x1, x2 = map(int, input().split())
rand_easy(m, seed, x1, x2)




'''
문제 접근 방식
- % m 을 하므로 a 와 c 가 m 보다 클 이유가 없음 그 뒤 완전탐색으로 시도

어려웠던 점
- 반복문이 이중 반복문이어서 break문을 사용할 수 없음 => 함수로 선언 return

설명이 필요한점

'''