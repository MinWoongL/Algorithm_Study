# 최빈수 구하기

import numpy as np
import scipy as sp
from collections import Counter


def modenumber(num):
    ct = Counter(num)
    ct_mode = ct.most_common(1)

    return ct_mode


testcase = int(input())

for i in range(testcase):
    index = int(input())
    number = list(map(int, input().split()))
    mode_num = modenumber(number)
    print("#{} {}".format(index, mode_num[0][0]))

