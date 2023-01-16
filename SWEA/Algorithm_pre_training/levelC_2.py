# 미로 2
import sys

sys.stdin = open('input.txt', "r")


def find_start_point(li): # 시작점을 찾는 함수, (x,y) == 2 인곳을 찾기
    x, y = 0, 0
    for i in range(0,100):
        for j in range(0,100):
            if li[i][j] == 2:
                x = i
                y = j
                break
    return [(x, y)]


def road_check(matrix):  # 경로탐색함수
    start_point = find_start_point(matrix)  # 시작위치찾기
    x, y = start_point[0][0], start_point[0][1]  # 시작위치저장
    route = [(x, y)]  # 앞으로 가야할 좌표저장
    past_road = [(x, y)]  # 이미 지나간 좌표저장
    dxy = [-1,1]  # xy 좌표이동을 위해 저장
    a = 0  # 정답저장
    while route:
        lx, ly = route.pop()  # 시작좌표 입력받기
        for i in range(2):  # x축 경로이동
            x_location = lx + dxy[i]
            if 0 <= x_location < 100:
                #  이동할 위치가 '길' 이고 이미 지나온 경로가 아닌경우에 좌표저장
                if matrix[x_location][ly] == 0 and (x_location,ly) not in past_road:
                    route.append((x_location, ly))
                    past_road.append((x_location, ly))
                elif matrix[x_location][ly] == 3:  # 도착점에 도착할시에 a=1 저장
                    a = 1
                    route.clear()
                    break
        for i in range(2):  # y축 경로이동
            y_location = ly + dxy[i]
            if 0 <= y_location < 100:
                if matrix[lx][y_location] == 0 and (lx,y_location) not in past_road:
                    route.append((lx, y_location))
                    past_road.append((lx, y_location))
                elif matrix[lx][y_location] == 3:
                    a = 1
                    route.clear()
                    break
    return a


for i in range(10):
    idx = int(input())
    mat = [list(map(int, input()))for _ in range(100)]
    answer = road_check(mat)
    print("#{} {}".format(idx, answer))
