# 11478_서로 다른 부분 문자열의 개수

s = input()
sli = []

for i in range(1,len(s)+1):  # i는 부분집합의 개수
    for j in range(len(s)+1-i):  # j는 부분집합의 개수만큼 슬라이싱 해줄 시작위치
        sli.append(s[j:j+i])

ss1 = set(sli)

print(len(ss1))