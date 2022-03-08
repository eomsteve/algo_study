# 1541 / 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

# 식 받아오기
arr = list(input())

# 받아온 식을 [ 숫자, 연산, 숫자, 연산, 숫자 ... ] 형태로 만들어주기
top = -1
int_arr = []    # 수를 담아줄 배열
cul_arr = []    # 연산자를 담아줄 배열

for idx in range(len(arr)):
    # 지금 보고있는 인덱스가 + or - 라면
    if ord(arr[idx]) == 43 or ord(arr[idx]) == 45:
        # 앞의 숫자를 계산식에 추가
        item = 0
        for i in range(top + 1):
            item += int(arr[idx - 1 - i]) * (10 ** i)
        int_arr.append(item)
        
        # 해당 인덱스의 연산자를 계산식에 추가
        cul_arr.append(arr[idx])
        top = -1
    
    # 끝까지 왔다면
    elif idx == len(arr) - 1:
        # 끝에있는 숫자 계산식에 추가
        item = 0
        for i in range(top + 1):
            item += int(arr[idx - 1 - i]) * (10 ** (i + 1))
        item += int(arr[idx])
        int_arr.append(item)
        top = -1
    else:
        top += 1

result = int_arr[0]
while i < len(cul_arr):
    if cul_arr[i] == '-':
        result -= int_arr[i + 1]
        for j in range(i + 1, len(cul_arr)):
            if cul_arr[j] == '-':
                i = j
                break
            else:
                result -= int_arr[j + 1]
                i = j + 1
    else:
        result += int_arr[i + 1]
        i += 1

print(result)

### 시간초과
### 접근방법
# 우선 받아온 리스트를 [ 숫자, 연산, 숫자, 연산, 숫자 ... ] 형태로 만든뒤
# 연산에 따라 최소값을 만들수 있도록 계산해주는 반복문을 작성하였으나
# 시간초과가 뜹니다 ..
# 받아온것을 위와같은 형태로 만드는 과정과 반복문을 합치면 가능할것같습니다 ..