# 6549_히스토그램에서 가장 큰 직사각형_histogram

import sys

test = True
while test:
    nli = list(map(int, sys.stdin.readline().split()))

    n = nli[0]
    if n == 0:
        test = False
        break
    nli = nli[1:]

    # print(nli)
    max_rec = 0
    width = 0
    number_of_rec = 0
    min_height = 1000000000
    n_stack = []
    pop_rec = []
    checker = 1
    for i in range(n):
        while n_stack and n_stack[-1] > nli[i]:
            pop_rec.append(n_stack.pop())
            checker += 1
            width -= 1
            if n_stack:
                j = 0
                checker_n = checker
                while j < len(n_stack) and n_stack[-(j+1)] >= nli[i]:
                    checker_n += 1
                    j += 1
                max_rec = max((len(pop_rec)+1)*n_stack[-1], max_rec, checker_n*nli[i])
            else:
                max_rec = max((width+len(pop_rec))*min_height, max_rec, (len(pop_rec)+1*nli[i]))
            checker = 1

        pop_rec.clear()
        n_stack.append(nli[i])
        if n_stack[-1] == 0:
            number_of_rec = 0
            continue
        else:
            if len(n_stack) == 1:
                min_height = nli[i]

            if nli[i] <= min_height:
                min_height = nli[i]

            width += 1
            number_of_rec += 1
            max_rec = max(nli[i], width * min_height, number_of_rec, max_rec)

    print(max_rec)