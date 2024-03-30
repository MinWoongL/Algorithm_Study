# 10986_나머지합_the remainder sum
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n_lst = list(map(int, input().split()))

cnt = 0

prefix = [0]
rest_dict = {0: 1}
for i in range(N):
    tmp = (prefix[-1] + n_lst[i])%M
    if tmp in rest_dict.keys():
        rest_dict[tmp] += 1
    else:
        rest_dict[tmp] = 1
    prefix.append(tmp)

for i in range(N+1):
    rest_dict[prefix[i]] -= 1
    cnt += rest_dict[prefix[i]]

print(cnt)