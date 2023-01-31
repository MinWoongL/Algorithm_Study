# 18870_좌표압축_coordinate-sorting

n = int(input())

coordi_li = list(map(int, input().split()))

s_li = sorted(coordi_li)  # 순서대로 딕셔너리에 넣어주기 위해 sorting
# print(s_li)
coordi_di = {}  # 중복제거를 위해 딕셔너리 형태로 저장
count = 0  # count 변수로 딕셔너리에 몇번째 저장 되었는지 저장 = 좌표압축순서
for v in s_li:
    if v not in coordi_di.keys():
        coordi_di[v] = count
        count += 1
# print(coordi_di)

for v in coordi_li:
    print(coordi_di[v], end=' ')