import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

tri = [a, b, c]
tri.sort()

if tri[0] + tri[1] <= tri[2]:
    tri[2] = (tri[0] + tri[1] - 1)

print(sum(tri))