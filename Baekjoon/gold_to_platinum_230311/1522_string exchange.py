# 1522_문자열교환_string exchange
import sys
input = sys.stdin.readline

init_value = input().rstrip()

tail = init_value.count('a')
left = init_value[:tail]

new_str = init_value+left

start = 0
ans = float('inf')
for i in range(len(init_value)):
    temp = new_str[i:i+tail]
    check = temp.count('b')
    if check < ans:
        ans = check

print(ans)