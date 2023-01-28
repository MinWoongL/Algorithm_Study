# 11866_요세푸스문제0_Josephus 0

from collections import deque

n, k = map(int, input().split())

dq = [] #  이 문제에서는 인덱스 넘버로 값을 제거할 필요가있음 deque는 불가능?
jose_li = []

new_k = k-1

for i in range(1,n+1):
    dq.append(i)

while len(dq) != 0:
    if new_k >= len(dq):
        # print('len(dq) = {}'.format(len(dq)))
        new_k = new_k % len(dq)  # arr의 길이로 나눈 나머지만큼 다시 앞부터 계산
        # print(new_k)
    jose_li.append(dq[new_k])
    dq.pop(new_k)
    # print(dq)
    # print(jose_li)
    new_k += k-1  # 값 하나를 제거한 후이니 k-1만큼 더해줘야함

# 출력 주의
print('<',end='')
for i in range(len(jose_li)):
    if i != (len(jose_li)-1):
        print(jose_li[i],end=', ')
    else:
        print('{}>'.format(jose_li[i]))

