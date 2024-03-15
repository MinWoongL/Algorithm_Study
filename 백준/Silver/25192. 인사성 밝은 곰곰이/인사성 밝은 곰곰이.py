import sys
input = sys.stdin.readline

N = int(input())

users = {}
cnt = 0
for _ in range(N):
    tmp = input().strip()
    if tmp == 'ENTER':
        users = {}
    else:
        if tmp in users.keys():
            continue
        else:
            users[tmp] = 1
            cnt += 1

print(cnt)