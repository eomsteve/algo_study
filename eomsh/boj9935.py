import sys
input = sys.stdin.readline

words = list(input().rstrip())
boom = list(input().rstrip())
stack = []

for i in words:
    stack.append(i)
    if len(stack) >= len(boom):
        if stack[-len(boom):] == boom:
            for _ in range(len(boom)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')