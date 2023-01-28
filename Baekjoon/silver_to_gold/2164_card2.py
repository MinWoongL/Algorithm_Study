# 2164_카드2_Card2

from collections import deque

n = int(input())
dq = deque()

for i in range(1, n+1):
    dq.append(i)

while len(dq) != 1:
    dq.popleft()  # 가장 위의 카드를 제거
    dq.append(dq.popleft())  # 가장 위의 카드를 가장 아래로 이동

print(dq[0])