answer = 0  # 모든 함수에서 글로벌 선언

def dfs(k, dungeons, cnt, visited):
    global answer

    if answer < cnt:
        answer = cnt

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:  # 피로도 충분하고, 방문하지 않은 곳
            visited[i] = 1
            dfs(k - dungeons[i][1], dungeons, cnt + 1, visited)
            visited[i] = 0

def solution(k, dungeons):
    global answer

    visited = [0] * len(dungeons)
    dfs(k, dungeons, 0, visited)

    return answer

'''
문제 접근 방식 : dfs, visted함수를 사용하여 dfs를 돌려 최대 방문 회수 구하기

어려웠던점 :

설명이 필요한점 : 
'''