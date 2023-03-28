# 1759_암호만들기_password
import sys
input = sys.stdin.readline


def make_word(n):
    if len(ans) == L:
        cnt = 0
        for i in range(L):
            if ans[i] in vowels:
                cnt += 1
        if 0 < cnt < L-1:
            print(*ans, sep='')
        else:
            return

    for i in range(n, C):
        ans.append(c_li[i])
        make_word(i+1)
        ans.pop()


L, C = map(int, input().split())

c_li = list(map(str, input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']

c_li.sort()
ans = []

make_word(0)

# # 1759_암호만들기_password (조합활용)
# import sys
# input = sys.stdin.readline
#
#
# def comb(li, n):
#     result = []
#     if n > len(li):
#         return result
#
#     if n == 1:
#         for i in li:
#             result.append([i])
#     else:
#         for i in range(len(li) - n + 1):
#             for j in comb(li[i+1:], n-1):
#                 result.append([li[i]] + j)
#
#     return result
#
#
# L, C = map(int, input().split())
#
# c_li = list(map(str, input().split()))
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# v = []
# c = []
#
# for value in c_li:
#     if value in vowels:
#         v.append(value)
#     else:
#         c.append(value)
#
# ans = []
# for i in range(1, len(v)+1):
#     if L-i >= 2:
#         v_lst = comb(v, i)
#         c_lst = comb(c, L-i)
#         for v1 in v_lst:
#             for v2 in c_lst:
#                 ans.append(v1+v2)
#
# s_ans = []
# for v in ans:
#     v.sort()
#     s_ans.append(''.join(v))
#
# s_ans.sort()
# for word in s_ans:
#     print(word)
