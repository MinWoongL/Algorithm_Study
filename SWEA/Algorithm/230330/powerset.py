# Powerset

def f(i, k, s, key, rs):
    global cnt
    global c
    c += 1
    if s == key:  # s(지금까지 합이)가 key와 같아졌다면 cnt 증가
        cnt += 1
    elif i == k or s > key or s+rs < key:  # 백트래킹 부분 : i==k(다 돌았는데도 key값이 안됬거나), s>key(이미 키 값을 넘어갔으면)
                                           # 또는 s+rs < key(s에 남은 모든 원소합을 더해도 key가 안되면)
        return
    else:
        bit[i] = 0
        f(i+1, k, s, key, rs-A[i])   # A[i] 미포함
        bit[i] = 1
        f(i+1, k, s+A[i], key, rs-A[i])  # A[i] 포함


A = [i for i in range(1, 11)]
N = 10
bit = [0]*N
key = 2
cnt = 0
c = 0
f(0, N, 0, key, sum(A))
print(cnt, c)

# elif 부분이 없으면 어떤 합을 탐색하든 cnt값이 같다 = 모든경우를 탐색한다.

