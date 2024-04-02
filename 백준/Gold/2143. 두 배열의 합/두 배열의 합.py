# 2143_두 배열의 합
import sys
input = sys.stdin.readline

T = int(input())

N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

m_dict = {}
cnt = 0

prefix_n = [0]
prefix_m = [0]
for i in range(N):
    prefix_n.append(prefix_n[-1] + n_lst[i])

for i in range(M):
    prefix_m.append(prefix_m[-1] + m_lst[i])

for i in range(M, -1, -1):
    for j in range(i):
        tmp = prefix_m[i] - prefix_m[j]
        if tmp in m_dict.keys():
            m_dict[tmp] += 1
        else:
            m_dict[tmp] = 1

for i in range(N, -1, -1):
    for j in range(i):
        tmp = prefix_n[i] - prefix_n[j]
        if T - tmp in m_dict.keys():
            cnt += m_dict[T-tmp]
        else:
            continue

print(cnt)
