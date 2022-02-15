while True:
    sentence = input().lower()
    if sentence == '#':
        break
    target = sentence[0]
    cnt = -1
    for chr in sentence:
        if chr == target:
            cnt += 1
    print(f'{target} {cnt}')
