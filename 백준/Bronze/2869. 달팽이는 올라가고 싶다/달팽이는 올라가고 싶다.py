import sys
import math
input = sys.stdin.readline

a, b, v = map(int, input().split())

print(1) if v == a else print(math.ceil((v-a) / (a-b))+1)