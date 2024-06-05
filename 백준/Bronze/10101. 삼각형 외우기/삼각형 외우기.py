import sys
input = sys.stdin.readline

tri = []
for _ in range(3):
    tri.append(int(input()))

if sum(tri) != 180:
    print('Error')
else:
    tri.sort()
    if tri.count(60) == 3:
        print('Equilateral')
    elif tri[0] == tri[1] or tri[1] == tri[2]:
        print('Isosceles')
    else:
        print('Scalene')