N, M = map(int, input().split())

lst = [i for i in range(1, N+1)]
for i in range(M):
    s, e = map(int, input().split())
    lst[e-1], lst[s-1] = lst[s-1], lst[e-1]

print(*lst)