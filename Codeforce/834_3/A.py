# A_Yes-Yes

T = int(input())
s = 'Yes'*100
for tc in range(T):
    test_s = str(input())

    if test_s in s:
        print('Yes')
    else:
        print('No')



