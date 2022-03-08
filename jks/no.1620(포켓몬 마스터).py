N, M = map(int, input().split())
arr = [input() for _ in range(N)]
for i in range(M):
    a = input()
    if a.isdigit():
        print(arr[int(a) - 1])
    else:
        print(arr.index(a) + 1)