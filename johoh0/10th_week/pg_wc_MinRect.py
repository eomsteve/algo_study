def solution(sizes):
    long = []  # 긴 부분 저장
    short = []  # 짧은 부분 저장
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:  # 가로가 긴 경우
            long.append(sizes[i][0])
            short.append(sizes[i][1])
        else:  # 세로가 긴 경우
            long.append(sizes[i][1])
            short.append(sizes[i][0])

    answer = max(long) * max(short)
    return answer

'''
문제 접근 방식 : 반복문을 사용하여 긴 값은 긴 값끼리, 짧은 값은 짧은 값끼리 모으고 
            각 배열의 최댓값끼리 곱하여 계산
어려웠던점 :

설명이 필요한점 : 
'''