# https://www.acmicpc.net/problem/1969
# DNA


N, M = map(int, input().split())
# DNA의 4가지 물질 사전순으로 나열
dna_4 = ['A', 'C', 'G', 'T']
# 4*M 개의 배열 생성(4종류 * M개)
arr = [[0 for _ in range(4)] for _ in range(M)]
hamming_dna = [0 for _ in range(M)]
hamming_sum = 0
for _ in range(N):
    dna = input()
    # 길이 M만큼 확인함
    for i in range(M):
        # 4가지 물질을 확인함
        for d in range(4):
            # A C G T 순으로 확인함
            if dna[i] == dna_4[d]:
                arr[i][d] += 1
# 해당 자릿수 마다 가장 많이 나온 알파벳을 hamming_dna에 담음
for i in range(M):
    max_val = 0
    for d in range(4):
        if max_val < arr[i][d]:
            max_val = arr[i][d]
            hamming_dna[i] = dna_4[d]
    # hamming distance는 N-최댓값 이므로 자릿수마다 더해줌
    hamming_sum += N - max_val
print(''.join(hamming_dna))
print(hamming_sum)



'''
문제 접근 방식
- 자리마다 가장 많이 나온 알파벳이 hamming의 알파벳이됨
- hamming distance는 N-최댓값 임

어려웠던 점
- dict로 풀려고 시도해 봤는데 dict는 순서가 없어서 그런지 오류가 나서 list로 다시 품

설명이 필요한점

'''