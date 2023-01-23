# 25305_커트라인

# 특별히 적을 주석이 없음


nk = list(map(int, input().split()))
s_li = list(map(int,input().split()))

s_li = sorted(s_li,reverse=True)

limit = s_li[nk[1]-1]
print(limit)