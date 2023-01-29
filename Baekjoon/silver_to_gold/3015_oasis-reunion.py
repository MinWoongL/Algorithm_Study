# 3015_오아시스 재결합_oasis_reunion
# 시간초과
import sys

N = int(input())
p_li = [sys.stdin.readline().strip() for _ in range(N)]
# print(p_li)

cnt_stack = []
ans = 0
for i in range(N):
    while cnt_stack and cnt_stack[-1][0] < p_li[i]:
        ans += cnt_stack.pop()[1]
        # print(cnt_stack)
        # print(ans)

    if cnt_stack and cnt_stack[-1][0] == p_li[i]:
        value = cnt_stack.pop()[1]
        ans += value
        # print(cnt_stack)
        # print(ans)

        if len(cnt_stack) != 0:
            ans += 1
        cnt_stack.append((p_li[i], value+1))
        # print(cnt_stack)
        # print(ans)
    else:
        if len(cnt_stack) != 0:
            ans += 1
        cnt_stack.append((p_li[i], 1))
        # print(cnt_stack)
        # print(ans)

print(ans)

'''  # 시간초과
p_stack = []
ans_li = [0] * N
ans = 0

p_stack.append(0)
for i in range(1, N):
    count = 1
    j = i
    while p_stack and p_li[p_stack[-1]] >= p_li[j] and j != (len(p_li)-1):
        count += 1
        j += 1
    ans_li[p_stack.pop()] = count
    ans += count
    p_stack.append(i)
    print(ans_li)

print(ans)
'''