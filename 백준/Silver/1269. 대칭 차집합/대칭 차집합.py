# 1269_대칭차집합_symmetric difference

import sys

A, B = map(int, input().split())

Ali = list(map(int, sys.stdin.readline().split()))
Bli = list(map(int, sys.stdin.readline().split()))

s1 = set(Ali)
s2 = set(Bli)

ss12 = s1^s2  # set 자료형을 이용하여 대칭 차집합을 구하는 방법
'''
s1.difference(s2) -> 차집합
s1.union(s2) -> 합집합
s1.intersection(s2) -> 교집합
'''

print(len(ss12))

