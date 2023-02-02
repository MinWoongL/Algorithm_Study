# 2447_별찍기_Recursion-starpoint

# 1. *을 찍는방식으로 재귀, 2. 완성된 matrix에서 *을 지우는 방식으로 재귀
def three_star_point(num):
    if num == 3:
        return ['***', '* *', '***']

    else:
        star_li = three_star_point(num//3)
        text = []

        for star in star_li:
            text.append(star*3)
            # print(text)

        for star in star_li:
            text. append(star+' '*(num//3)+star)

        for star in star_li:
            text.append(star*3)

        return text


n = int(input())

ans = three_star_point(n)
# print(ans)
print('\n'.join(ans))



# def star(l):
#     if l == 3:
#         return ['***','* *','***']
#
#     arr = star(l//3)
#     stars = []
#
#     for i in arr:
#         stars.append(i*3)
#
#     for i in arr:
#         stars.append(i+' '*(l//3)+i)
#
#     for i in arr:
#         stars.append(i*3)
#
#     return stars
#
# print('\n'.join(star(n)))



# for i in range(n):
#     for j in range(n):
#         if i < n/3:
#             print("*", end='')
#         elif i <= 2*n/3:
#             if j >= n/3 and j < 2*n/3:
#                 print(' ', end='')
#             else:
#                 print('*', end='')
#         else:
#             print('*', end='')
#     print('')



# def three_star_point(matrix):
#     ln = len(matrix[0])
#     global divide_num
#     if divide_num == ln:
#         return 1
#     else:
#         sli_y = ln//divide_num
#         while sli_y < ln-sli_y:
#             for i in range(sli_y, 2*sli_y):
#                 sli_x = ln // divide_num
#                 while sli_x < ln-sli_x:
#                     for j in range(sli_x, 2*sli_x):
#                         matrix[i][j] = ' '
#                     sli_x += ln//divide_num
#             sli_y += ln//divide_num
#
#         divide_num = divide_num*3
#         return three_star_point(matrix)
# n = int(input())
#
# divide_num = 3
#
# star_matrix = [['*'for i in range(n)] for i in range(n)]
#
# three_star_point(star_matrix)
#
# for v in star_matrix:
#     print(*v)