def solution(s):
    words = s.split(" ")  # 공백을 기준으로 단어를 나눔
    result = []

    for word in words:
        txt = ''
        for i in range(len(word)):
            if i % 2 == 0 :
                txt += word[i].upper()
            else:
                txt += word[i].lower()
        result.append(txt)

    return ' '.join(result)