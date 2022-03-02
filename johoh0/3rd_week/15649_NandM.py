# 15649 N 과 M (1)
N, M = map(int, input().split())

result = []  # 결과 리스트 초기화
used = [0] * (N+1)  # 1부터 N까지만 사용
def sol():  # dfs방식 이용
    if len(result) == M:  # M의 길이를 가지면 return
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):  # 1부터 N까지 순열 만들기
        if not used[i]:
            used[i] = 1
            result.append(i)
            sol()  # 재귀
            result.pop()
            used[i] = 0

sol()

'''
문제 접근 방식 : 수업시간에 배운 순열을 참고하여,
dfs방식으로 하나 추가하고 재귀 돌린 후 다시 삭제하고 다른 루트 찾는 방식

어려웠던점:

설명이 필요한점: 
'''

