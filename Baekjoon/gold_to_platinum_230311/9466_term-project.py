# 9466_텀프로젝트-term-project
# 시간초과
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    choice = list(map(int, input().split()))

    team = 0
    v = [0]*(N+1)
    for i in range(N):
        check = [0]*(N+1)
        cnt = 0
        if v[i] == 0:
            s = [i]
            while s:
                node = s.pop()
                if not check[choice[node]-1]:
                    s.append(choice[node]-1)
                    check[choice[node]-1] = 1
                    cnt += 1
            if check[i] == 1:
                team += cnt
                for j in range(N+1):
                    v[j] = check[j]
    print(N-team)

