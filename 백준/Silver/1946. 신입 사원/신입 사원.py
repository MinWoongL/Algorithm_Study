# 1946_신입사원_New-recruit
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())

    people = [list(map(int, input().split())) for _ in range(N)]

    people.sort(key=lambda x: x[0])

    cnt = 1
    score = people[0][1]
    for i in range(1, N):
        if people[i][1] < score:
            cnt += 1
            score = people[i][1]

    print(cnt)
