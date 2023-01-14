# 1대1 가위바위보
a, b = map(int, input().split())
if a != 1:
    if a>b:
        print('A')
    else:
        print('B')
elif b==3:
    print('A')
else:
    print('B')
