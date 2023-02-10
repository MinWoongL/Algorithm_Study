# 15652_N과M4

# 조합 재귀 함수
def comb(li, n):
    result = []
    if n > len(li):
        return result

    if n == 1:
        for i in li:
            result.append([i])
    else:
        # 1~n 모두 시작값에 넣기위해 범위 len(li)
        for i in range(len(li)):
            # 시작범위를 i+1 에서 i로 변경 - 자기자신 조합도 넣기위해서
            for j in comb(li[:], n-1):
                # 모든경우의 수 중 오름차순인 경우만 결과값에 넣기
                if j[0] >= li[i]:
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

ans = comb(num_li, M)
for v in ans:
    print(*v)

