import sys
input = sys.stdin.readline

check = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

while True:
    text = input().strip()
    if text == "#":
        break
    ans = 0
    for t in text:
        if t in check:
            ans += 1
    print(ans)
