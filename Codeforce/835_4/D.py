# D_Challenging_Valley
import sys

T = int(input())

for tc in range(T):
    ai = int(input())
    ai_li = list(map(int, sys.stdin.readline().split()))

    status = 0
    idx = 0
    for i in range(1, len(ai_li)):
        if ai_li[i] - ai_li[i-1] > 0:
            status = 1
            idx = i-1
            break
    if status == 0:
        print('YES')
    else:
        checker = True
        for j in range(idx+1, len(ai_li)):
            if ai_li[j] - ai_li[j-1] < 0:
                checker = False
        if checker:
            print('YES')
        else:
            print('NO')




    # if ai == 1:
    #     print('YES')
    # else:
    #     status = 0
    #     status_2 = 0
    #     checker = -1
    #     for i in range(len(ai_li) - 1):
    #         if ai_li[i] != ai_li[i + 1]:
    #             checker = i
    #             break
    #     if checker == -1:
    #         print('NO')
    #     else:
    #         if ai_li[checker+1] - ai_li[checker] < 0:
    #             status -= 1
    #         elif ai_li[checker+1] - ai_li[checker] > 0:
    #             status += 1
    #
    #         if status == 1:
    #             for i in range(checker + 1, len(ai_li)):
    #                 if ai_li[i] - ai_li[i - 1] < 0:
    #                     print('NO')
    #                     break
    #         else:
    #             if len(ai_li) == 2:
    #                 print('YES')
    #             else:
    #                 idx = 0
    #                 yes = 0
    #                 for j in range(checker + 1, len(ai_li) - 1):
    #                     if ai_li[j + 1] - ai_li[j] > 0:
    #                         idx = j
    #                         break
    #                 for k in range(idx + 1, len(ai_li)):
    #                     if ai_li[k] - ai_li[k - 1] < 0:
    #                         print('NO')
    #                         yes -= 1
    #                         break
    #                 if yes == 0:
    #                     print('YES')








