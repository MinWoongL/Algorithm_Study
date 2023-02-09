# 1026_보물_treasure

# B는 재배열하지 않고 A만 재배열해서 풀기
N = int(input())

Ali = list(map(int, input().split()))
Bli = list(map(int, input().split()))

ans = 0
Ali.sort()
for i in range(N):
    a = Ali[i]
    b = Bli.pop(Bli.index(max(Bli)))

    ans += a*b

print(ans)

