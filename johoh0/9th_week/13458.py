# 백준 13458 시험 감독

def sol():
    res = 0

    for i in range(N):
        if arr[i] > 0:
            arr[i] -= main
            res += 1

        if arr[i] > 0:
            res += arr[i]//sub

            if arr[i] % sub != 0:  # 나머지 값들도 더해준다.
                res += 1

    return res

N = int(input())
arr = list(map(int, input().split()))
main, sub = map(int, input().split())
print(sol())

'''
문제 접근 방식 : 함수를 만들어 정, 부 감독관 각각의 경우들을 더해준다.

어려웠던점 :

설명이 필요한점 : 
'''