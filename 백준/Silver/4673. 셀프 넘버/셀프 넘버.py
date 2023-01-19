def fn_d(n):  # n의 제네레이터들을 출력해줍니다.
    a = 0
    b = n
    while n>=1:
        a = a + n%10
        n = n//10
    return a+b


def is_selfnumber(n):  # n이 셀프넘버인지 판별해줍니다.
    selfnumli = []
    for i in range(1,n+1):
        ans = fn_d(i)
        if ans not in selfnumli:
            selfnumli.append(ans)
    for i in range(1,n+1):
        if i not in selfnumli:
            print(i)

is_selfnumber(10000)