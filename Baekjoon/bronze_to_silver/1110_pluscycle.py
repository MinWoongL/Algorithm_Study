#  더하기 사이클
#  시간 초과 났음

num = int(input())

changed = 0
count = 0
text = str(num)

while changed != num:
    c = str(int(text[-1]) + int(text[0]))
    # changed = int(text[-1]+c[-1])
    changed = int(''.join(text[-1], c[-1]))
    text = str(changed)
    count += 1


print(count)