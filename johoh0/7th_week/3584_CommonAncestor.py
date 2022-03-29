# def make_lst(ch, n):
#     for i in range(1, N):
#         if edges[i][1] == ch:
#             if n == 1:
#                 lst1.append(edges[i][0])
#                 make_lst(edges[i][0], 1)
#             else:
#                 lst2.append(edges[i][0])
#                 make_lst(edges[i][0], 2)
#
# def find_anc():
#     res = 0
#     for i in range(len(lst1)):
#         for j in range(len(lst2)):
#             if lst1[i] == lst2[j]:
#                 res = lst1[i]
#                 return res
# T = int(input())
#
# for _ in range(1, T+1):
#     N = int(input())
#     edges = [[0, 0]] + [list(map(int, input().split())) for _ in range(N-1)]
#     node1, node2 = map(int, input().split())
#     lst1 = [node1]
#     lst2 = [node2]
#     for i in range(1, N):
#         if edges[i][1] == node1:
#             lst1.append(edges[i][0])
#             make_lst(edges[i][0], 1)
#
#         if edges[i][1] == node2:
#             lst2.append(edges[i][0])
#             make_lst(edges[i][0], 2)
#
#     print(find_anc())

'''
문제 접근 방식 : 두 개의 출발 노드의 조상 리스트들을 구하여 비교 

어려웠던점 : 런타임 에러 (RecursionError)

설명이 필요한점 : 
'''
def find_anc():
    res = 0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                res = lst1[i]
                return res

T = int(input())

for _ in range(1, T+1):
    N = int(input())
    parents = [0] * (N+1)  # 부모 노드 초기화
    for _ in range(N-1):
        p, c = map(int, input().split())
        parents[c] = p  # 부모노드 저장

    node1, node2 = map(int, input().split())
    lst1 = [node1]
    lst2 = [node2]

    while parents[node1]:  # 제일 조상 노드는 0이므로 종료됨
        lst1.append(parents[node1])
        node1 = parents[node1]

    while parents[node2]:
        lst2.append(parents[node2])
        node2 = parents[node2]

    print(find_anc())

'''
문제 접근 방식 : 두 개의 지정 노드의 부모들을 구하여 비교

어려웠던점:

설명이 필요한점: 
'''