N = int(input())
for i in range(1, N+1):
    str_list = list(map(int, str(i)))
    if i + sum(str_list) == N:
        print(i)
        break
else:
    print(0)