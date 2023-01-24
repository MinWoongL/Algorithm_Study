import sys

T = int(sys.stdin.readline())
word_li = []
s_word_li = []

for i in range(T):
    word = str(sys.stdin.readline().strip())  # strip() 함수로 공백문자열 제거
    if word not in word_li:  # 입력 중복 제거
        word_li.append(word)

for v in word_li:
    s_word_li.append([len(v), v])  # 글자수 항목을 추가

s_word_li.sort()  # 정렬 시 먼저 글자수의 길이(첫 항)로 정렬 후 알파벳순(두번째 항)으로 정렬된다
for value in s_word_li:
    print(value[1])