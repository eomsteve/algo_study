# https://www.acmicpc.net/problem/2751
# 수 정렬하기2


import sys

n = int(input())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
for i in sorted(lst):
    sys.stdout.write(str(i)+'\n')



'''
문제 접근 방식
- input과 output을 sys로 받아주고 sorted를 사용(해결)

어려웠던 점
- 배열에 입력을 추가하고, 정렬해서, for문으로 출력을 하려했는데 시간초과가 뜸
정렬 알고리즘을 비교했을 때 가장 수행시간이 작은 정렬이 필요, 병합정렬을 사용 시간초과
병합 정렬에서 합병 시 append, extend함수와 슬라이싱을 없애 봤지만 시간초과가 뜸
input과 output을 sys로 받아주고 sorted를 사용(해결)
But 내장함수를 쓰지 않고 해결 못함.

설명이 필요한점
- sorted와 병합 정렬 모두 O(nlogn)의 시간복잡도를 가진다는데 왜 안되는지 모르겠음.

'''