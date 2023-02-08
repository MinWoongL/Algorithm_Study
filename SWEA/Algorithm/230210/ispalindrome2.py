# 회문2_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    word_mat = [list(map(str, input())) for _ in range(100)]
    print(word_mat)

    ans_li = [0]

    # for i in range(100):
    #     for j in range(50):
    #         if word_mat[i][j] == word_mat[i][99-j]:
    #             check = True
    #             k = j
    #             while True:
    #                 if k <= len(word_mat[0])//2 and word_mat[i][k] == word_mat[i][99-k]:
    #                     if k == len(word_mat[0])//2:
    #                         break
    #                     else:
    #                         k += 1
    #                 else:
    #                     check = False
    #                     break
    #             if check:
    #                 if (100-2*j) > len(ans_li):
    #                     ans_li.clear()
    #                     for v in range(j, 100-j):
    #                         ans_li.append(word_mat[i][v])
    #
    #         if word_mat[j][i] == word_mat[99-j][i]:
    #             check = True
    #             k = j
    #             while True:
    #                 if k <= len(word_mat[0])//2 and word_mat[k][i] == word_mat[99-k][i]:
    #                     if k == len(word_mat[0]) // 2:
    #                         break
    #                     else:
    #                         k += 1
    #                 else:
    #                     check = False
    #                     break
    #             if check:
    #                 if (100-2*j) > len(ans_li):
    #                     ans_li.clear()
    #                     for v in range(j, 100-j):
    #                         ans_li.append(word_mat[v][i])
    #
    # print(ans_li)
    # print(len(ans_li))

    for i in range(100):
        for j in range(100):
            for j2 in range(100-j):
                if word_mat[i][j] == word_mat[i][99 - j2]:
                    check = True
                    k = j
                    k2 = j2
                    while True:
                        if k + k2 + j <= 99 and word_mat[i][k] == word_mat[i][99 - k2]:
                            k += 1
                            k2 += 1
                        else:
                            if k + k2 + j > 99:
                                break
                            else:
                                check = False
                                break
                    if check:
                        if (100 - j - j2) > len(ans_li):
                            ans_li.clear()
                            for v in range(j, 100 - j2):
                                ans_li.append(word_mat[v][i])

                if word_mat[j][i] == word_mat[99 - j2][i]:
                    check = True
                    k = j
                    k2 = j2
                    while True:
                        if k + k2 + j <= 99 and word_mat[k][i] == word_mat[99 - k2][i]:
                            k += 1
                            k2 += 1
                        else:
                            if k + k2 + j > 99:
                                break
                            else:
                                check = False
                                break
                    if check:
                        if (100 - j - j2) > len(ans_li):
                            ans_li.clear()
                            for v in range(j, 100 - j2):
                                ans_li.append(word_mat[v][i])

    print(ans_li)
    print(len(ans_li))

