# 1700_멀티탭 스케줄링_multitab scheduling
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
appliances = list(map(int, input().split()))

using_app = set()
cnt = 0
ans = 0

next_use = {}

for i in range(K):
    if appliances[i] not in next_use.keys():
        next_use[appliances[i]] = []
    else:
        next_use[appliances[i]].append(i)


for i in range(K):
    tmp = appliances[i]
    if appliances[i] in using_app:
        next_use[tmp].pop(0)
        continue
    else:
        if cnt != N:
            using_app.add(tmp)
            cnt += 1
        else:
            change = [-1, -1]
            for s in using_app:
                if not next_use[s]:
                    using_app.remove(s)
                    using_app.add(tmp)
                    break
                else:
                    if next_use[s][0] > change[1]:
                        change = [s, next_use[s][0]]
            else:
                next_use[change[0]].pop(0)
                using_app.remove(change[0])
                using_app.add(tmp)
            ans += 1

print(ans)
