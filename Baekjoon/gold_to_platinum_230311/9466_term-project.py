# 9466_텀프로젝트-term-project
import sys
input = sys.stdin.readline
T = int(input())

def dfs(node, visited, cycle):
    visited[node] = True
    cycle.append(node)
    while True:
        node = cycle[-1]
        next_node = choice[node]-1
        if visited[next_node]:
            if next_node in cycle:
                return cycle[cycle.index(next_node):]
            else:
                return []
        else:
            visited[next_node] = True
            cycle.append(next_node)

for tc in range(T):
    N = int(input())
    choice = list(map(int, input().split()))

    team = [0]*(N+1)
    visited = [False]*(N+1)

    for i in range(N):
        if not visited[i]:
            cycle = []
            cycle = dfs(i, visited, cycle)

            for node in cycle:
                team[node] = 1

    print(N-sum(team))


