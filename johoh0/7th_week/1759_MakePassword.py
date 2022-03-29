# 백준 1759 암호만들기
# https://www.acmicpc.net/problem/1759

def dfs(idx, tmp_len, tmp_arr):
    if tmp_len == L:
        vow = 0  # vowel 모음
        con = 0  # consonent 자음
        for i in range(L):
            if tmp_arr[i] in 'aeiou':
                vow += 1
            else:
                con += 1
        # 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
        if vow >= 1 and con >= 2:
            print(''.join(tmp_arr))
        return

    for i in range(idx, C):
        selected[i] = 1
        tmp_arr.append(lst[i])
        dfs(i+1, tmp_len + 1, tmp_arr)
        tmp_arr.pop(-1)
        selected[i] = 0


L, C = map(int, input().split())  # L: 암호의 길이, C: 문자의 종류 개수
lst = list(map(str, input().split()))
# 암호는 알파벳이 증가하는 순서로 배열
lst.sort()
selected = [0] * C
dfs(0, 0, [])

'''
문제 접근 방식 : 정렬하여 하나씩 더하여 부분함수만드는 재귀함수를 만든다.

어려웠던점: 

설명이 필요한점: 
'''