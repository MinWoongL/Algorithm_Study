# 1110_더하기사이클

num = int(input())

changed = 0
count = 0

if num < 10:  # 한자리 수 인경우 앞에 0을 붙여주는 작업 추가
    text = '0'+str(num)
else:
    text = str(num)

if num == 0:
    print(1)
else:
    while changed != num:
        c = str(int(text[-1]) + int(text[0]))
        # changed = int(text[-1]+c[-1])
        changed = str(text[-1]) + c[-1]  # int형으로 먼저 바꿔주면 '05' 가 5로 저장됨
        text = changed
        changed = int(changed)
        count += 1

    print(count)


