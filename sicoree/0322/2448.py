N = int(input())
arr = [[' '] * (N * 2 - 1) for _ in range(N)]

for row in arr:
    for star in row:
        print(star, end = '')
    print()