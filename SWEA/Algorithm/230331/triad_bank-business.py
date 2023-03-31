# SWEA_정식이의 은행업무

def b_to_d(n):
    num = 0
    check = 0
    for i in range(len(n)-1, -1, -1):
        if n[i] == '1':
            num += 2**check
        check += 1

    return num


def t_to_d(n):
    num = 0
    check = 0
    for i in range(len(n)-1, -1, -1):
        if n[i] != '0':
            num += int(n[i])*(3**check)
        check += 1

    return num


T = int(input())

for tc in range(1, T+1):
    binary = input()
    triad = input()

    num_li = []
    ans = 0
    for i in range(len(binary)):
        if binary[i] == '0':
            word = binary[:i] + '1' + binary[i+1:]
            num_li.append(b_to_d(word))
        else:
            word = binary[:i] + '0' + binary[i+1:]
            num_li.append(b_to_d(word))

    for j in range(len(triad)):
        check = False
        for k in range(3):
            if triad[j] != str(k):
                word = triad[:j] + str(k) + triad[j+1:]
                ans = t_to_d(word)
                if ans in num_li:
                    check = True
                    break
        if check:
            break

    print(f'#{tc} {ans}')
