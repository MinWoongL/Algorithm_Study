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