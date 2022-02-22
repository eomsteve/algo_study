N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
n = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                if arr[i][0] + arr[j][1] + arr[k][2] + arr[l][3] == 0:
                    n += 1
print(n)
'''
문제접근방식 : 하나하나 다 확인.. 너무 단순한데 더 멋진 방식이 생각이 안나네요ㅜㅜ

어려웠던점: 시간 초과ㅠㅠ

설명이 필요한점?
'''