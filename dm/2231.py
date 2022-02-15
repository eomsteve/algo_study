# https://www.acmicpc.net/problem/2231
# 분해합


N = int(input())

make_list = []
for i in range(1, N+1):
    sum_val = i
    for s in str(i):
        sum_val += int(s)
    make_list.append(sum_val)

if N in make_list:
    print(make_list.index(N)+1)
else:
    print(0)



'''
문제 접근 방식
- 원래값 + 각 자리수의 합을 가지는 가장 작은 숫자이므로, 그 이하의 list를 만들어
index를 이용해 첫 번째 칭구를 찾아봄.

어려웠던 점
- 일의자리 칭구들은 생성자가 자기자신인줄 알았는데 자기자신 + 1의 자리 숫자를 더해
2배가 됩니다! ex) 3 = 생성자가 3인줄 오해했는데 사실을 3+3=6, 생성자가 6이 됩니다!

설명이 필요한점

'''