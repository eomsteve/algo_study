eng = []
while eng != ['#']:
    eng = list(input().split().lower())
    k = eng[0]
    eng_sum = 0
    for i in range(1, len(eng)):
        for j in range(len(eng[i])):
            if k == eng[i][j]:
                eng_sum += 1
    if k != '#':
        print(k, eng_sum)