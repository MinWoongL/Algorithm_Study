import sys
input = sys.stdin.readline

# sample = ['AAAA', 'BB']
board = input().strip()
counter = 0

tmp_b = board.replace("XXXX", "AAAA")
tmp_b = tmp_b.replace("XX", "BB")
# print(tmp_b)

if 'X' in tmp_b:
    print(-1)
else:
    print(tmp_b)
