# 백준 14889 스타트와 링크

def dfs(idx, cnt):
    global res
    if cnt == N // 2:
        s, l = 0, 0
        for i in range(N):
            for j in range(N):
                # 반반이 되었을 때 팀 전력들 구하기
                if selected[i] and selected[j]:
                    s += S[i][j]
                elif not selected[i] and not selected[j]:
                    l += S[i][j]
        res = min(res, abs(s - l))  # 결과값을 최소값 재정리

    for i in range(idx, N):
        selected[i] = 1
        dfs(i + 1, cnt + 1)  # 재귀하여 풀어주기
        selected[i] = 0

# 입력 받기
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
res = 100*20*200  # 결과값 초기화
selected = [0]*N
dfs(0, 0)

print(res)

'''
문제 접근 방식 : dfs, 포함 여부 추가하며 값 더하고 비교

어려웠던점: python 시간초과 / pypy 통과

설명이 필요한점: 
'''