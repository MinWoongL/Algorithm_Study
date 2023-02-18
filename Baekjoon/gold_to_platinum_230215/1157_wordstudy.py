# 1157_단어공부_wordstudy

s = str(input())

s_di = {}

for v in s:
    if v.upper() not in s_di.keys():
        s_di[v.upper()] = 1
    else:
        s_di[v.upper()] += 1

s_li = []
for k, v in s_di.items():
    s_li.append([k, v])

s_li.sort(key=lambda x: x[1],reverse=True)

if len(s_li) == 1:
    print(s_li[0][0])
elif s_li[0][1] == s_li[1][1]:
    print('?')
else:
    print(s_li[0][0])

