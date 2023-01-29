# 17298_오큰수_NGE

# *list 출력 -> 공백을 구분으로 리스트 안의 모든 값 출력

from collections import deque
import sys

n = int(input())

nli = list(map(int, sys.stdin.readline().split()))

ans_li = [-1] * n  # 오큰수가 없는경우 -1 반환을 위해 default값으로 설정
idx_stack = deque()

idx_stack.append(0)  # idx 0 을 넣은 상태로 시작

for i in range(1, n):
    # if idx_stack:  # while문에서 index가 남아있는지 확인을 같이 해야함.
    while idx_stack and nli[idx_stack[-1]] < nli[i]:  # 현재 index가 오큰수가 되는 모든 idx_stack값에 값을 반환
        ans_li[idx_stack.pop()] = nli[i]
    idx_stack.append(i)
# print(ans_li)
print(*ans_li)  # 공백으로 구분하여 리스트 안의 값들을 출력





