N, M = map(int, input().split())
DNA = []
for _ in range(N):
    DNA.append(input())
# A,T,G,C 카운트해서 많은거 하나씩 추가
result = ''
cnt = 0
for j in range(M):
    arr = [0] * 26 # 알파벳 26개 리스트 만들고 카운트
    for i in range(N):
        arr[ord(DNA[i][j])-65] += 1 # ord('A') 가 65이므로 A가 0번째 인덱스가 되기위해 -65 해줌
    result += chr(arr.index(max(arr)) + 65)
for nc in DNA: # DNA의 뉴클레오타이드 안의 각 문자열을 반복하면서 다르면 카운트 +1 해준다
    for k in range(M):
        if nc[k] != result[k]:
            cnt += 1
print(result)
print(cnt)

'''
어려운 점: 처음에는 주어진 DNA 하나를 기준 잡고 각각 문자열 차이 구해서 차이가 가장 적게 나오는 DNA 구하는 건 줄 알았는데
가장 빈도수 높은 알파벳들 뽑은 후 차이를 구하는 거였다.
또 처음에는 a,c,t,g [0] 리스트 4개 만들어서 풀려고 하니 카운트하고 나서 max 값의 인덱스와 A,C,T,G 를 연관지을 방법이
없어서 되게 시간을 많이 썼는데 알파벳 리스트 26개 만들어서 ord chr 하면 가능해서 ord chr로 풀었다.
문제 이해하는 것도 시간이 오래걸렸고 푸는 것도 시간 오래 걸렸음
'''