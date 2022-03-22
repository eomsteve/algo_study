# https://www.acmicpc.net/problem/1107
# 리모컨


N = int(input())
M = int(input())
if M:
    wrong_b = input().split()
else:
    wrong_b = []
ch = abs(100 - N)

for i in range(1000001):
    for j in str(i):
        if j in wrong_b:
            break
    else:
        ch = min(ch, len(str(i))+abs(N-i))
print(ch)
