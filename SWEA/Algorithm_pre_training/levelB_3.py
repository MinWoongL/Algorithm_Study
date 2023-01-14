#두 개의 숫자열
import sys

sys.stdin = open('input.txt', "r")

def N_M(N, M, N_list, M_list):
    max_ans = 0
    if N < M:
        for i in range(0, M-N+1):
            ans = 0
            for j in range(0, N):
                ans = ans + (N_list[j] * M_list[j+i])
            max_ans = max(ans,max_ans)
    else:
        for i in range(0, N-M+1):
            ans = 0
            for j in range(0, M):
                ans = ans + (N_list[j+i] * M_list[j])
            max_ans = max(ans, max_ans)

    return max_ans


TC = int(input())

for i in range(1, TC+1):
    NM = list(map(int,input().split()))
    N = NM[0]
    M = NM[1]
    N_list = list(map(int,input().split()))
    M_list = list(map(int,input().split()))

    ans = N_M(N,M,N_list,M_list)

    print("#{} {}".format(i,ans))


