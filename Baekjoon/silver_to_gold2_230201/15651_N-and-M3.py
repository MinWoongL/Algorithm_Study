# 15651_N과M3

def comb(li, n):
    result = []
    if n > len(li):
        return result

    if n == 1:
        for i in li:
            result.append([i])
    else:
        for i in range(len(li) - n + 1):
            for j in comb(li[i+1:], n-1):
                result.append([li[i]] + j)

    return result


# 순열 재귀 함수
def perm(li, n):
    result = []
    if n > len(li):
        return result

    if n == 1:
        for i in li:
            result.append([i])
    else:
        for i in range(len(li)):
            ans = [i for i in li]
            # 중복을 허용해주기 위해 본인을 제외하는 줄 삭제
            # ans.remove(li[i])
            for k in perm(ans, n-1):
                result.append([li[i]]+k)

    return result


N, M = map(int, input().split())

num_li = []

for i in range(1, N+1):
    num_li.append(i)

ans = perm(num_li, M)
for v in ans:
    print(*v)

