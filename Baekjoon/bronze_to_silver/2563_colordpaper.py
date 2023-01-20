#  색종이 - 한번에 맞춘문제! -

T = int(input())

white = [[0 for i in range(100)] for j in range(100)]  # 하얀색 빈 색종이 저장

cord = [list(map(int,input().split()))for i in range(T)]  # 검정 색종이의 좌표 저장

for cordi in cord:  # 검정 색종이가 놓이는 위치를 1로 바꿔줌
    x, y = cordi[0], cordi[1]
    for i in range(x, x+10):
        for j in range(y, y+10):
            if white[i][j] == 0:
                white[i][j] = 1
area = 0  # 1이 적힌 영역을 세기 위한 변수
for i in range(100):
    n = white[i].count(1)
    area += n

print(area)

