N = int(input())
arr = [list(input()) for _ in range(N)]
n = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 0
            if i > 0:
                if arr[i-1][j] == 0 or arr[i-1][j] == 'R':
                    continue
            elif i < N - 1:
                if arr[i+1][j] == 0 or arr[i+1][j] == 'R':
                    continue
            elif j > 0:
                if arr[i][j-1] == 0 or arr[i][j-1] == 'R':
                    continue
            elif j < N - 1:
                if arr[i-1][j] == 0 or arr[i-1][j] == 'R':
                    continue
            else:
                n += 1
        elif arr[i][j] == 'G':
            arr[i][j] = 1
            if i > 0:
                if arr[i-1][j] == 1 or arr[i-1][j] == 'G':
                    continue
            elif i < N - 1:
                if arr[i+1][j] == 1 or arr[i+1][j] == 'G':
                    continue
            elif j > 0:
                if arr[i][j-1] == 1 or arr[i][j-1] == 'G':
                    continue
            elif j < N - 1:
                if arr[i-1][j] == 1 or arr[i-1][j] == 'G':
                    continue
            else:
                n += 1
        elif arr[i][j] == 'B':
            arr[i][j] = 2
            if i > 0:
                if arr[i-1][j] == 2 or arr[i-1][j] == 'B':
                    continue
            elif i < N - 1:
                if arr[i+1][j] == 2 or arr[i+1][j] == 'B':
                    continue
            elif j > 0:
                if arr[i][j-1] == 2 or arr[i][j-1] == 'B':
                    continue
            elif j < N - 1:
                if arr[i-1][j] == 2 or arr[i-1][j] == 'B':
                    continue
            else:
                n += 1
        print(arr)
        print(n)