# 2841 외계인의 기타 연주
import sys
sys.stdin = open('guitar.txt', 'r')

N, P = map(int, input().split())  # N: 음의 수, P: 프렛의 수
arr = [[] for _ in range(7)]  # 기타 눌러야할 배열 초기화(기타는 1~6번줄, 0번 안씀)

cnt = 0  # 손가락을 붙이거나 떼는 변화 횟수 초기화
for _ in range(N):
    l, p = map(int, input().split())  # l: 줄의 번호, p: 줄의 프렛
    if not arr[l]:  # 초기 상태
        arr[l].append(p)
        cnt += 1
    elif arr[l]:  # 값이 있는 상태
        if arr[l][-1] < p:  # 같은 줄의 프렛이 증가할 경우 누르는 경우이니 추가하며 cnt += 1
            arr[l].append(p)
            cnt += 1
        else:
            while arr[l] and arr[l][-1] > p:  # 프렛 값이 감소할 경우 삭제하며 cnt += 1
                arr[l].pop()
                cnt += 1
            if arr[l] and arr[l][-1] == p:  # 프렛 값이 같다면 현상 유지 후 continue
                continue
            arr[l].append(p)  # 높은 값 손을 떼고 내려온 경우 낮은 값 추가하고 cnt += 1
            cnt += 1

print(cnt)
# python 시간 초과 pypy 통과
'''
문제 접근 방식 : 같은 줄인 경우 새로운 pret이 올라가는 경우 append, 새로운 pret이 내려가는 경우 넘는 숫자들 pop
append, pop 때 변화가 있다보고 cnt 1 증가시켜줌

어려웠던점: pypy는 통과했는데 python으로 시간초과한 점

설명이 필요한점: 
'''