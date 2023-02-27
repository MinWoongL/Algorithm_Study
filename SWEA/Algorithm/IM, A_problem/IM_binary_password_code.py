# IM_단순2진암호코드_서울2반_이민웅

code_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}


def code_check(lst):
    ans = 0
    number_sum = 0
    odd_even = True
    for k in range(0, len(lst), 7):
        check = lst[k:k+7]
        ch = ''
        for v in range(len(check)):
            ch = ch + str(check[v])
        if ch in code_dict.keys():
            num = code_dict[ch]
            if odd_even:
                ans += num*3
                number_sum += num
                odd_even = False
            else:
                ans += num
                number_sum += num
                odd_even = True

    return [ans, number_sum]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    code = [list(map(int, input())) for _ in range(N)]

    code_start = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if code[i][j] == 1:
                code_start.append(i)
                code_start.append(j)
                break
        if code_start:
            break

    real_code = code[code_start[0]][code_start[1]-55:code_start[1]+1]

    password = code_check(real_code)

    if password[0] % 10 == 0:
        print(f'#{tc} {password[1]}')
    else:
        print(f'#{tc} 0')










