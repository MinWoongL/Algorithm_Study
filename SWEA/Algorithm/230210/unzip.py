# 압축풀기_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    zipli = [[0 for i in range(10)]for i in range(10)]
    max_num = 0
    for v in range(n):
        word, num = map(str, input().split())
        if int(num) > max_num:
            max_num = int(num)
        zipli.append([word, int(num)])

    print(zipli)




