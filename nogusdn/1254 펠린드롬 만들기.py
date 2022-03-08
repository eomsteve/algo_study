s = input()
cnt = 0
for i in range(len(s)):
    pal = s[i:]
    if pal == pal[::-1]:
        print(cnt+len(s))
        break
    else:
        cnt += 1