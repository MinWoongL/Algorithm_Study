# 10986_나머지합_the remainder sum
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n_lst = list(map(int, input().split()))

cnt = 0
prefix = [0]
rest_dict = {0: 1}

for i in range(N):
    tmp = (prefix[-1] + n_lst[i]) % M
    cnt += rest_dict.get(tmp, 0)
    rest_dict[tmp] = rest_dict.get(tmp, 0) + 1
    prefix.append(tmp)

print(cnt)