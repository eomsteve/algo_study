n = int(input())
RGB = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    RGB[i][0] += min(RGB[i-1][1], RGB[i-1][2])
    RGB[i][1] += min(RGB[i-1][0], RGB[i-1][2])
    RGB[i][2] += min(RGB[i-1][0], RGB[i-1][1])

print(min(RGB[n-1][0], RGB[n-1][1], RGB[n-1][2]))

# 누적된 것의 최소값을 선택해야한다