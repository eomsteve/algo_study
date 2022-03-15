# https://www.acmicpc.net/problem/1918
# 후위 표기식


cal = ['+', '-', '*', '/', '(']
isp_lst = [1, 1, 2, 2, 0]
isp, icp = {}, {}
for i in range(len(cal)):
    isp[cal[i]] = icp[cal[i]] = isp_lst[i]
    if cal[i] == '(':
        icp[cal[i]] = 3
# 중위표기식의 토큰을 하나씩 읽어오기
# data = '2+3*4/5'
data = input()
stack = []
for i in range(len(data)):
    if data[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        print(data[i], end='')
    elif data[i] in '*/+-(':
        if not stack:
            stack.append(data[i])
        else:   # 스택이 비어있지 않으면
            # 내가 작거나 같으면 우선순위를 비교해 다뻄
            if isp[stack[-1]] >= icp[data[i]]:
                while stack and isp[stack[-1]] >= icp[data[i]]:
                    print(stack.pop(), end='')
            stack.append(data[i])
    # 3. 닫는 괄호는 여는 괄호가 나올때 까지 pop
    else:
        if not stack:
            break 
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
# 스택에 남은 녀석을 pop
while stack:
    print(stack.pop(), end='')
print()
