# 1967_트리의지름_diameter-of-tree
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

for _ in range(N-1):
    n1, n2, w = map(int, input().split())

    tree[n1].append([n2, w])
    tree[n2].append([n1, w])  # 트리는 원래 무향그래프이지만 역방향 재탐색을 위해 추가

# print(tree)
m_weight, m_node = bfs(1)
ans_weight, ans_node = bfs(m_node)

print(ans_weight)
