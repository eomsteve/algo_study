def generate(arr, idx, chosen):
    if len(chosen) == L:
        vowel = 0
        for i in vowels:
            if chosen.count(i):
                vowel += 1
        if vowel > 0 and L - vowel > 1:
            print(''.join(chosen))
            return
    if idx == C:
        return
    chosen.append(arr[idx])
    generate(arr, idx + 1, chosen)
    chosen.pop()
    generate(arr, idx + 1, chosen)
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
generate(arr, 0, [])