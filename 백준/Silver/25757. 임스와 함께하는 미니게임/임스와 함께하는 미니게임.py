# 25757_임스와 함께하는 미니게임_ImsMinigame
import sys
input = sys.stdin.readline

games = {
    'Y': 2,
    'F': 3,
    'O': 4
}

N, G = input().split()
N = int(N)

max_user = games[G]
user_list = {}
count = 1
ans = 0

for _ in range(N):
    user = input()
    if user in user_list.keys():
        continue
    else:
        user_list[user] = 0
        count += 1
        if count == max_user:
            ans += 1
            count = 1

print(ans)