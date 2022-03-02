s = list(input().split('-'))
a = []
total = 0
for word in s:
    plus = sum(list(map(int, word.split('+'))))
    a.append(plus)
total += a[0]

for i in range(1, len(a)):
    total -= a[i]

print(total)