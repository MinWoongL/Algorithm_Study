# 15889_호 안에 수류탄이야
import sys
input = sys.stdin.readline

N = int(input())

*n_cordi, = map(int, input().split())
if N > 1:
    n_range = list(map(int, input().split()))
    st = [n_cordi[0] + n_range[0]]

    for i in range(1, N - 1):
        if n_cordi[i] <= st[-1]:
            if n_cordi[i] + n_range[i] > st[-1]:
                st[-1] = n_cordi[i] + n_range[i]
        else:
            break

    if n_cordi[-1] <= st[-1]:
        ans = "권병장님, 중대장님이 찾으십니다"
    else:
        ans = "엄마 나 전역 늦어질 것 같아"
else:
    ans = "권병장님, 중대장님이 찾으십니다"

print(ans)