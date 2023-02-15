# 11000_강의실배정_Lecture-room
import sys
from collections import deque
import heapq

N = int(sys.stdin.readline())
ans_li = []

lecture = []
end_time = deque()
hq = []

for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())
    lecture.append([s, t])
lecture.sort(key=lambda x: x[0])
# print(lecture)

end_time.append(lecture[0][1])
heapq.heappush(hq, lecture[0][1])
# print(end_time)
for i in range(1, len(lecture)):
    # if lecture[i][0] < end_time[0]:
    #     if lecture[i][1] >= end_time[0]:
    #         end_time.append(lecture[i][1])
    #     else:
    #         end_time.appendleft(lecture[i][1])
    # else:
    #     end_time.popleft()
    #     end_time.append(lecture[i][1])
    #     end_time = deque(sorted(end_time))
    if lecture[i][0] < hq[0]:
        heapq.heappush(hq, lecture[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq, lecture[i][1])
print(len(hq))