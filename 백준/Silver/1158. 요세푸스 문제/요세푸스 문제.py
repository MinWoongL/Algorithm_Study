T = list(map(int, input().split()))

N = T[0]
K = T[1]

Num_list = []
for i in range(1, N+1):
    Num_list.append(i)

num = 0
sol = []
for j in range(N):
    num += K -1
    if num >= len(Num_list):
        num = num%len(Num_list)
        
    sol.append(str(Num_list.pop(num)))


new =', '.join(sol)

print('<' + new + '>', sep = '')
