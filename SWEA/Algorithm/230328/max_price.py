# SWEA_최대상금

T = int(input())

for tc in range(1, T+1):
    num_pad, c = map(int, input().split())

    num = []
    num.append(str(num_pad))

    for _ in range(c):
        s_li = num
        check = []
        while True:
            if not s_li:
                break
            s = list(s_li.pop())

            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    s[i], s[j] = s[j], s[i]
                    check.append(''.join(s))
                    s[i], s[j] = s[j], s[i]
        check = set(check)
        num = list(check)

    check = list(map(int, check))

    print(f'#{tc} {max(check)}')
