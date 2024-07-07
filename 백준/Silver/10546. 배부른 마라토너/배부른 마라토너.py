import sys
input= sys.stdin.readline

N = int(input())
li = dict()
for _ in range(N):
    name = input().rstrip() #출전명단
    if name not in li.keys(): #선수가 딕셔너리 key 값에 없으면
        li[name] = 1 #1로 하고
    else:
        li[name] += 1 #동명이인이 존재하면 value값을 1 증가시킨다.


for _ in range(N-1):
    name = input().rstrip() #완주명단
    if name in li.keys(): #완주했으면 value값을 1 증가시켜준다.
        li[name] += 1

for key, values in li.items():
    if values %2 == 1: #만약 1명이 출전해서 1명이 완주했으면 value값이 2여야되는데, 2명이 출전해서
  #1명만 완주하면 value값이 3이다. 이런식으로 미완주자를 찾는다.
        print(key)
        break