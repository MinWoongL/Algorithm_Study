# SWEA_수영장_swimming-pool

def bt(s, cost):
    global ans
    if s >= 12:
        if cost < ans:
            ans = cost
        return

    if cost >= ans:
        return

    bt(s+1, cost+month)
    bt(s+1, cost+(plan[s]*day))
    bt(s+3, cost+t_month)


T = int(input())

for tc in range(1, T+1):

    day, month, t_month, year = map(int, input().split())

    plan = list(map(int, input().split()))

    ans = year

    bt(0, 0)
    print(f'#{tc} {ans}')
