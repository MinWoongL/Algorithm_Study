time = list(map(int, input().split()))
cooking_time = int(input())

finished_time = time[1] + cooking_time

if finished_time >= 60:
    min = finished_time%60
    hour = finished_time//60
    time[0] += hour
    time[1] = min
else:
    time[1] = finished_time  # 이 부분을 +=로 해서 오답을 받음

if time[0] >= 24:
    time[0] = time[0]-24

print("{} {}".format(time[0],time[1]))