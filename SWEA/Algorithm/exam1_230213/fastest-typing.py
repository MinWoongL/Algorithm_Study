T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    N = len(A)  # 타이핑할 문자열 길이
    M = len(B)  # 단축패턴

    cnt = 0
    idx = 0

    while N-idx > M:
        if A[idx] == B[0]:
            for i in range(M):
                if A[idx+i] != B[i]:
                    idx += 1
                    cnt += 1
                    break
            else:
                idx += M
                cnt += 1
        else:
            idx += 1
            cnt += 1
    if N-idx < M:
        cnt += N-idx
    else:
        if A[idx:] == B:
            cnt += 1
        else:
            cnt += N-idx
    print(f'#{tc} {cnt}')

