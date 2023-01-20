T = int(input())

white = [[0 for i in range(100)] for j in range(100)]

cord = [list(map(int,input().split()))for i in range(T)]

for cordi in cord:
    x, y = cordi[0], cordi[1]
    for i in range(x, x+10):
        for j in range(y, y+10):
            if white[i][j] == 0:
                white[i][j] = 1
area = 0
for i in range(100):
    n = white[i].count(1)
    area += n

print(area)