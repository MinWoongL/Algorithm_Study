# 2110_공유기설치_Install-router
# 알고리즘 구분 참조했음
import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())

houses = []
ans = 0
for _ in range(N):
    houses.append(int(input()))

houses.sort()

# 공유기가 2개면 무조건 정렬된 상태의 양 끝
if C == 2:
    ans = houses[N-1] - houses[0]
# 3개 이상일 경우 가능한 최대 거리의 절반부터 이분탐색으로 원하는 공유기 개수만큼 설치가가능한지 판단
else:
    min_dis = 1
    max_dis = houses[N-1] - houses[0]
    while min_dis <= max_dis:
        cnt = 0
        router = houses[0]
        mid = (min_dis + max_dis)//2

        for i in range(1, N):
            if houses[i]-mid >= router:
                cnt += 1
                router = houses[i]
        if cnt >= C-1:
            min_dis = mid + 1
            ans = mid
        else:
            max_dis = mid - 1
print(ans)


