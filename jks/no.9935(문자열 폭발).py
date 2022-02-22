arr = list(input())
rm = list(input())
for r in rm:
    c = arr.count(r)
    for i in range(c):
        arr.remove(r)
if len(arr) == 0:
    print('FRULA')
else:
    print(''.join(arr))

'''
문제접근방식 : arr에 rm이 있으면 갯수만큼 지움

어려웠던점: 시간 초과ㅠㅠ

설명이 필요한점? 
'''