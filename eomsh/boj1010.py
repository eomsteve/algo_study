n = int(input())
peoples = [input().split() for _ in range(n)]
peoples.sort(key=lambda a: int(a[0]))
for i in peoples:
    print(f'{i[0]} {i[1]}')

'''
문제접근방식 : 

어려웠던점:

설명이 필요한점?
'''