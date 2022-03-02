S = list(input())
mid = len(S)//2
if len(S) % 2:
    for i in range(mid, len(S)-1):
        if S[i-1] == S[i+1]:
            for j in range(2, mid-i+1):
                if S[i-j] != S[i+j]:
                    break
            else:
                print(2*i+1)
                break
        if S[i] == S[i+1]:
            for j in range(2, mid-i+1):
                if S[i-j+1] != S[i+j]:
                    break
            else:
                print(2*i+2)
                break
    else:
        print(4*mid-1)
else:
    for i in range(mid, len(S)-1):
        if S[i-1] == S[i]:
            for j in range(1, mid-i):
                if S[i-j-1] != S[i+j]:
                    break
            else:
                print(2*i)
                break
        if S[i-1] == S[i+1]:
            for j in range(1, mid-i):
                if S[i-j] != S[i+j]:
                    break
            else:
                print(2*i+1)
                break
    else:
        print(4*mid-1)

'''
문제접근방식 : 가운데를 시작으로 기준값~끝값이 기준값 이전에도 반복되는지 확인. 반복된다면 조건에 맞게 길이 출력

어려웠던점: 인덱싱 헷갈림...

설명이 필요한점?
'''