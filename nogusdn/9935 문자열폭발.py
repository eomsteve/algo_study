# 재귀 느낌으로
# t = input()
# p = input()
# def function(t, p):
#     if p in t:
#         return function(t.replace(p, ''), p)
#     else:
#         if t:
#             return t
#         else:
#             return 'FRULA'
#
# print(function(t,p))

# 그냥 반복문
# t = input()
# p = input()
# while True:
#     if p in t:
#         result = t.replace(p, '')
#         t = result
#     else:
#         if t:
#             print(t)
#             break
#         else:
#             print('FRULA')
#             break
#

# 스택으로

t = input()
p = input()
stack = []
for i in range(len(t)):
    stack.append(t[i]) # stack에 추가
    if stack[-1] == p[-1] and len(stack) >= len(p): # stack의 마지막 요소와 p의 마지막 요소가 같고 stack이 p 길이 이상 쌓였으면
        if ''.join(stack[-len(p):]) == p: # stack 끝의  p길이 만큼의 값과 p가 일치하면 BOOM
            for j in range(len(p)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')


'''
처음에 재귀로 풀었는데 메모리 초과 떠서 반복문으로 푸니 시간초과가 떳다.
그래서 stack으로 겨우 풀었다.
'''