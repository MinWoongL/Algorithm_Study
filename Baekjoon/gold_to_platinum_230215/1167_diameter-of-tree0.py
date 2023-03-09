# 1167_트리의지름0_diameter-of-tree0
import sys
from collections import deque
input = sys.stdin.readline


def bfs(n):
    max_w = 0
    max_w_node = 0

    q = deque()
    q.append([n, 0])
    visited = [-1] * (N + 1)
    visited[n] = 0
    while q:
        c_node, w = q.popleft()
        visited[c_node] = w
        for c, weight in tree[c_node]:
            if visited[c] == -1:
                w_sum = w + weight
                q.append([c, w_sum])
                visited[c] = w_sum

                if w_sum > max_w:
                    max_w = w_sum
                    max_w_node = c

    return max_w, max_w_node


N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N):
    n_li = list(map(int, input().split()))
    n_li.pop()
    for i in range(1, len(n_li), 2):
        tree[n_li[0]].append([n_li[i], n_li[i+1]])

# print(tree)
m_weight, m_node = bfs(1)
ans_weight, ans_node = bfs(m_node)

print(ans_weight)
