# 1969 DNA
import sys
sys.stdin = open('DNA.txt', 'r')

N, M = map(int, input().split())  # N: DNA의 수, M: 문자열의 길이
arr = [list(input()) for _ in range(N)]  # 배열 초기화
print(arr)

result = ''  # 결과 값 result 초기화
ham_d = 0  # 해밍 거리
for j in range(M):  # 가로열 고정
    cnt = [0, 0, 0, 0] # DNA A, C, G, T 각 개수 초기화
    for i in range(N):  # 세로열의 문자 개수 찾기
        if arr[i][j] == 'A':
            cnt[0] += 1
        elif arr[i][j] == 'C':
            cnt[1] += 1
        elif arr[i][j] == 'G':
            cnt[2] += 1
        elif arr[i][j] == 'T':
            cnt[3] += 1

    max_v = 0
    for i in range(len(cnt)):  # cnt 중 최고 개수 찾기
        if max_v < cnt[i]:
           max_v = cnt[i]

    if max_v == cnt[0]:  # max_v가 동일한 경우가 있으면 사전 순이므로 A, C, G, T 순으로 조건문을 설정
        result += 'A'
        ham_d += cnt[1]+cnt[2]+cnt[3]
    elif max_v == cnt[1]:
        result += 'C'
        ham_d += cnt[0]+cnt[2]+cnt[3]
    elif max_v == cnt[2]:
        result += 'G'
        ham_d += cnt[0]+cnt[1]+cnt[3]
    elif max_v == cnt[3]:
        result += 'T'
        ham_d += cnt[0]+cnt[1]+cnt[2]

print(result)
print(ham_d)
'''
문제 접근 방식 : 문자열을 이중 배열로 입력을 받아 세로열마다 글자마다의 개수를 세서 최대 값을 구하고
 최대 값에 해당하는 문자와 문자와 다른 수 만큼을 출력

어려웠던점: 

설명이 필요한점: 생각나는 대로 해서 코드 간소화?
'''