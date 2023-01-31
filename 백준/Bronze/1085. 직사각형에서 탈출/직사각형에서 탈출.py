# 1085_직사각형에서 탈출_escape-from-Rectangle
import sys

x, y, w, h = map(int, sys.stdin.readline().split())

print(min(w-x, h-y, x, y))
