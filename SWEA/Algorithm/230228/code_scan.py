# 암호코드스캔_서울2반_이민웅_1단계까지 풀이

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
code_dict2 = [[3, 2, 1, 1],
              [2, 2, 2, 1],
              [2, 1, 2, 2],
              [1, 4, 1, 1],
              [1, 1, 3, 2],
              [1, 2, 3, 1],
              [1, 1, 1, 4],
              [1, 3, 1, 2],
              [1, 2, 1, 3],
              [3, 1, 1, 2],
              ]


def make_binary_range(s):
    idx = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            idx = i
            break
    ans_li = []
    for i in range(idx - 55, idx + 1, 7):
        text = s[i:i + 7]
        if text in code_dict.keys():
            ans_li.append(code_dict[text])

    return ans_li


def num_check(lst):
    ans = 0
    number_sum = 0
    odd_even = True
    for i in range(len(lst)):
        if odd_even:
            ans += int(lst[i])*3
            number_sum += int(lst[i])
            odd_even = False
        else:
            ans += int(lst[i])
            number_sum += int(lst[i])
            odd_even = True

    return [ans, number_sum]


def sixteen_to_two(s):
    num1 = int(s, 16)
    ans = ''
    for j in range(3, -1, -1):
        bit = 1 if num1 & (1 << j) else 0
        ans = ans + str(bit)
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    mat = [list(map(str, input())) for _ in range(N)]
    result_sum = 0
    column = M - 1
    x = 0
    binary_s_dict = {}
    while True:
        if x == N-1:
            break
        else:
            sub_lst = []
            empty = False
            column_check = 10000000
            for j in range(M - 1, -1, -1):
                if mat[x][j] != '0':
                    if column_check - j < 14:
                        continue
                    else:
                        column_check = j

                        for k in range(0, j + 1):
                            sub_lst.append(mat[x][k])

                        binary_s = ''
                        for i in range(len(sub_lst) - 15, len(sub_lst)):
                            s = sixteen_to_two(sub_lst[i])
                            binary_s += s
                        if binary_s not in binary_s_dict.keys():
                            binary_s_dict[binary_s] = 0
                            rest = ''
                            for i in range(0, len(sub_lst) - 15):
                                rest += sub_lst[i]

                            binary_s = rest + binary_s

                            idx = 0
                            for i in range(len(binary_s) - 1, -1, -1):
                                if binary_s[i] == '1':
                                    idx = i
                                    break

                            ans_li = make_binary_range(binary_s)

                            result = num_check(ans_li)

                            if result[0] % 10 == 0:
                                result_sum += result[1]
            x += 1

    print(f'#{tc} {result_sum}')

