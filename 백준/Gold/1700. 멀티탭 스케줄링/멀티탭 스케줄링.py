# 1700_멀티탭 스케줄링_multitab scheduling
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
appliances = list(map(int, input().split()))

using_app = set()
cnt = 0
ans = 0

for i in range(K):
    tmp = appliances[i]
    if appliances[i] in using_app:
        continue
    else:
        if cnt != N:
            using_app.add(tmp)
            cnt += 1
        else:
            tmp_set = set(k for k in using_app)
            for j in range(i+1, K):
                if len(tmp_set) == 1:
                    break
                if appliances[j] in tmp_set:
                    tmp_set.remove(appliances[j])
            change = tmp_set.pop()
            using_app.remove(change)
            using_app.add(tmp)
            ans += 1

print(ans)
