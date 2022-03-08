# 9095 1, 2, 3 더하기
import sys
sys.stdin = open('123plus.txt', 'r')

def sol():
    global cnt, sum_v
    if sum_v == n:  # 더한 값이 n일 경우 cnt + 1하고 return
        cnt += 1
        return
    for i in range(1, 4):  # 1 ~ 3까지 더해줌
        if sum_v + i <= n:
            sum_v += i
            sol()
            sum_v -= i

T = int(input())  # 전체 tc 개수

for tc in range(1, T+1):
    n = int(input())
    sum_v = 0
    cnt = 0
    sol()
    print(cnt)

'''
문제 접근 방식 : dfs 방식으로 sum_v와 cnt를 글로벌 선언
    sum_v는 합이 n이 될 때까지 이용, cnt는 sum_v가 n일 경후 +1하여 카운트

어려웠던점:

설명이 필요한점: 
'''