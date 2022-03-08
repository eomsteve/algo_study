# 1969_DNA
# https://www.acmicpc.net/problem/1969

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
result = [0] * M
DNA_dict = { 0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}

result_sum = 0
for i in range(M):
    # ['A', 'C', 'G', 'T']
    DNA_list = [0] * 4
    for j in range(N):
        if arr[j][i] == 'A':
            DNA_list[0] += 1
        elif arr[j][i] == 'C':
            DNA_list[1] += 1
        elif arr[j][i] == 'G':
            DNA_list[2] += 1
        elif arr[j][i] == 'T':
            DNA_list[3] += 1

    max_DNA = 0
    for idx in range(4):
        if DNA_list[max_DNA] < DNA_list[idx]:
            max_DNA = idx

    result_sum += N - DNA_list[max_DNA]
    result[i] = DNA_dict[max_DNA]
print(''.join(result))
print(result_sum)

##### 접근방법
# N * M 의 DNA 배열에서 각 열의 최다 DNA를 찾아 result에 넣어주는 방식
#
##### 어려웠던점
# 문제를 이해하는것에 한세월이 걸렸다 ..