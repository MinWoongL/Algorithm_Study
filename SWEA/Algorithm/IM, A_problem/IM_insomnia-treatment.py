# 호석이의 불면증 치료법

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    num_dict = {}
    num = N
    cnt = 0
    while True:
        if len(num_dict) == 10:
            break
        else:
            cnt += 1
            s_n = str(num)
            for v in range(len(s_n)):
                if s_n[v] not in num_dict.keys():
                    num_dict[s_n[v]] = 0
        num += N
    print(f'#{tc} {num-N}')

