# 2751_수 정렬 2

# 시간초과 - 정렬 시 시간복잡도를 줄이는 방법을 알아야함.
# sys.stdin.readline 을 사용하면 for문 안의 input 함수 사용보다 시간을 줄일 수 있음
# 시간복잡도가 O(nlogn)인 정렬 알고리즘을 사용해야한다.

import sys

T = int(input())
li = []

for i in range(T):
    n = int(sys.stdin.readline())  # int로 감싸주어야 함
    li.append(n)
li = sorted(li)

# for v in li:
#     print(v)

for i in range(T):
    print(li[i])
