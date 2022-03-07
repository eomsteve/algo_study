# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
dic = {}
# dic 으로 입력을 받음
for i in range(1, N+1):
    voca = input().rstrip()
    i = str(i)
    dic[i] = voca
    dic[voca] = i
for _ in range(M):
    print(dic[input().rstrip()])

'''
# list로 입력을 받아봤는데 시간초과가 났음, list의 경우 인자를 찾는데 걸리는 시간이 O(N)인 반면 딕셔너리는 O(1)이어서 시간복잡도가 빠름
'''