# 8980_택배_parcel

N, truck = map(int, input().split())
n = int(input())
package_li = []
for _ in range(n):
    s, g, p = map(int, input().split())
    package_li.append([s, g, p, p / (g - s)])

village = [0] * (N - 1)
ans = 0

package_li.sort(key=lambda x: x[3], reverse=True)
print(package_li)

for v in package_li:
    for i in range(v[0] - 1, v[1] - 1):
        check = False
        if village[i] + v[2] <= truck:
            village[i] += v[2]
            check = True
        if check:
            ans += v[2]

print(village)
print(int(ans))
