import sys
input = sys.stdin.readline

dial_info = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
number = input().strip()
min_time = 0

for t in range(len(number)):
    for i in range(len(dial_info)):
        if number[t] in dial_info[i]:
            min_time += (i+3)
print(min_time)