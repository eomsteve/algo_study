# 1620. 나는야 포켓몬 마스터 이다솜
# 문제 설명이 좀.... 많이 웃김

N, M = map(int, input().split())  # N: 포켓몬 개수 / M : 맞춰야할 수

poke_dict = {}  # dict 사용
for i in range(1, N+1):  # 도감은 1번부터
    name = input()
    poke_dict[i] = name  # 쌍으로 저장
    poke_dict[name] = i

# print(poke_dict)
for _ in range(M):  # 찾아야하는 것들  굳이 i 안써도 될 듯?
    find = input()
    if find.isalpha():  # 문자일 경우
        print(poke_dict[find])  # 도감 넘버 출력
    else:  # 숫자일 경우
        print(poke_dict[int(find)])  # 이름 출력

'''
문제 접근 방식 : dict를 사용하여 쌍으로 입력하기.... 그리고 출력해야할 것들 문자인지 숫자인지 구별하여 dict에서 출력

어려웠던점: pypy3로 통과 
isalpha 또는 isdigit을 써야했는데 자주 쓰지 않아 떠올리기 힘들었던 점?

설명이 필요한점: 
'''