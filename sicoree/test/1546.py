import sys
sys.stdin = open('1546.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

max_val = 0

for idx in arr:
    if max_val < idx:
        max_val = idx


S_arr = 0
for idx in arr:
    S_arr += (idx * 100) / max_val

E_arr = S_arr / N
print(E_arr)