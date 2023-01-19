#  그룹 단어 체커

tn = int(input())
count = 0
for i in range(tn):
    li = []
    checker = True
    text = str(input())
    for j in range(1, len(text)):  # 두번째 글자부터 이전 글자와 같은지 확인
        if text[j] == text[j - 1]:
            pass
        else:
            if text[j - 1] not in li:  # 다르다면 그 글자가 이전에 사용되었는지 확인
                li.append(text[j - 1])
            else:  # 사용되었으면 이 단어는 그룹단어가 아니다
                checker = False

    if text[-1] in li:  # 마지막단어를 한번 더 체크해줘야 함.
        checker = False

    if checker is True:
        count += 1
    print(count)
