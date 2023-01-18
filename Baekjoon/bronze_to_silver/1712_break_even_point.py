# 손익분기점
def break_even_point(a,b,c):  # a:고정비용, b:가변비용, c:가격책정
    if b >= c:
        return -1
    else:
        return int(a // (c - b) + 1)


num = list(map(int, input().split()))

print(break_even_point(num[0],num[1],num[2]))
