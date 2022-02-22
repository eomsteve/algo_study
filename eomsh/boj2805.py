import sys
input = sys.stdin.readline


N, M = map(int, input().split())
n_num = list(map(int, input().split()))
n_num.sort()


def bin_search(m, m_arr):
    start = 0
    end = m_arr[-1]
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in m_arr:
            if (i - mid) > 0:
                total += (i - mid)
        if m > total:
            end = mid - 1
        if m <= total:
            start = mid + 1
            result = mid
    return result


print(bin_search(M, n_num))